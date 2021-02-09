import boto3
import json
import logging

from botocore.exceptions import ClientError

"""
    1. Get instance ID from ec2
    2. Start the instance
    3. Register the instance to CLB
"""

ec2_client = boto3.client('ec2')
clb_client = boto3.client('elb')
instance_id_list = []


def get_instances_by_tag(instance_state):
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'Peak',
                ]
            },
            {
                'Name': 'instance-state-name',
                'values': [
                    instance_state.lower(),
                ]
            }
        ]
    )
    print(response)

    # Process response to get instance id
    total_instances = len(response.get('Reservations')[0].get('Instances'))
    count = 0
    while count < total_instances:
        instance_id = response.get('Reservations')[0].get('Instance')[count].get('InstanceId')
        instance_id_list.append(instance_id)

        count = count + 1
    print(instance_id_list)


def start_instance(instance_id_list):
    # do a dryrun first to verify permissions
    try:
        ec2_client.start_instances(
            InstanceIds=instance_id_list,
            DryRun=True
        )
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            logging.error(e)
            raise

        # Dry run succeeded, run start_instance without dryrun
        try:
            response = ec2_client.start_instances(
                InstanceIds=instance_id_list,
                DryRun=False
            )
            logging.info('Instance start action response: {}'.format(response))
        except ClientError as e:
            logging.error(e)
        return response


def stop_instance(instance_id_list):
    # do a dryrun first to verify permissions
    try:
        ec2_client.stop_instances(
            InstanceIds=instance_id_list,
            DryRun=True
        )
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            logging.error(e)
            raise

        # Dry run succeeded, run stop_instance without dryrun
        try:
            response = ec2_client.stop_instance(
                InstanceIds=instance_id_list,
                DryRun=False
            )
        except ClientError as e:
            logging.error(e)
        return response


def register_instance(instance_id_list):
    list_of_instance_id = []
    count = 0
    while count < len(instance_id_list):
        list_of_instance_id.append(
            {
                'InstanceId': instance_id_list[count]
            }
        )
        count = count + 1

    response = clb_client.register_instance_with_load_balancer(
        LoadBalancerName='demo-clb',
        Instances=list_of_instance_id
    )
    logging.info('Register Instance to CLB response: {}'.format(response))
    return response


def de_register_instance(instance_id_list):
    list_of_instance_id = []
    count = 0
    while count < len(instance_id_list):
        list_of_instance_id.append(
            {
                'InstanceId': instance_id_list[count]
            }
        )
        count = count + 1
    response = clb_client.deregister_instances_from_load_balancer(
        LoadBalancerName='demo-clb',
        Instances=list_of_instance_id
    )
    print('Deregister instance to clb response {}'.format(response))
    return response


def main():
    # get_instances_by_tag('Running')
    # start_instance(instance_id_list)
    # stop_instance(instance_id_list)
    # response = register_instance(instance_id_list)
    response = de_register_instance(instance_id_list)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


if __name__ == '__main__':
    main()
