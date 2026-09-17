import argparse 
from google.cloud import storage

def main():
    parser = argparse.ArgumentParser(description='Create a Google Cloud Storage bucket.')
    parser.add_argument('bucket_name', type=str, help='The name of the bucket to create.')
    args = parser.parse_args()

    bucket_name = args.bucket_name
    print("Bucket name received:{bucket-name}")
    # Aquí puedes agregar la lógica para crear el bucket usando la biblioteca de Google Cloud Storage.

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"  # Puedes cambiar la clase de almacenamiento según tus necesidades.
    new_bucket = storage_client.create_bucket(bucket, location="us-central1")  # Puedes cambiar la ubicación según tus necesidades. 
    print(f'Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}.'   )

if __name__ == '__main__':
    main()