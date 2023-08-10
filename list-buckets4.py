import boto3

# Crear un cliente de S3 en la región 'us-east-1'
s3 = boto3.client('s3', 'us-east-1')

# Nombre del archivo local que deseas subir
local_file_path = 'archivo.txt'

# Nombre deseado para el archivo en el bucket de S3
s3_file_key = 'archivo.txt'

# Nombre del bucket en el que deseas subir el archivo
bucket_name = 'tallerb1laura'

# Subir el archivo al bucket
s3.upload_file(local_file_path, bucket_name, s3_file_key)

print(f'Archivo {local_file_path} subido exitosamente a {s3_file_key} en el bucket {bucket_name}')

