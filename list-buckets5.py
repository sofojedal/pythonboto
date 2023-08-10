import boto3

# Crear un cliente de S3 en la región 'us-east-1'
s3 = boto3.client('s3','us-east-1')

# Nombre deseado para el archivo en tu sistema local
local_file_path = 'archivoDescargado.txt'

# Nombre del archivo en el bucket de S3 que deseas descargar
s3_file_key = 'archivo.txt'

# Nombre del bucket desde el que deseas descargar el archivo
bucket_name = 'tallerb2laura'

# Descargar el archivo desde el bucket
s3.download_file(bucket_name, s3_file_key, local_file_path)

print(f'Archivo descargado exitosamente desde {s3_file_key} en el bucket {bucket_name} y guardado en {local_file_path}')

