import os
import subprocess

env_map = {
    'aws_access_key_id': 'AWS_ACCESS_KEY_ID',
    'aws_secret_access_key': 'AWS_SECRET_ACCESS_KEY',
    'aws_session_token': 'AWS_SESSION_TOKEN',
    'region': 'AWS_DEFAULT_REGION',
}

new_env = dict(os.environ)

with open('/workspace/credentials') as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('['):
            k, v = line.split('=', 1)
            k = k.strip().lower()
            v = v.strip()
            if k in env_map:
                new_env[env_map[k]] = v

# Copy credentials directly to standard AWS config path
subprocess.run(['mkdir', '-p', '/root/.aws'], env=new_env)
subprocess.run(['cp', '/workspace/credentials', '/root/.aws/credentials'], env=new_env)

# Authenticate kubeconfig
subprocess.run(['aws', 'eks', 'update-kubeconfig', '--name', 'cluster', '--region', 'us-east-1'], env=new_env)

# Execute init.sh to map IAM roles
subprocess.run(['bash', '/workspace/setup/init.sh'], env=new_env)

# Output deployments, services, pods
subprocess.run(['kubectl', 'get', 'pods,services,deployments'], env=new_env)