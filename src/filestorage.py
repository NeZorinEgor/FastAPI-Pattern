from contextlib import asynccontextmanager
from typing import Optional

from src.settings import settings

from aiobotocore.session import get_session


class S3Client:
    def __init__(
            self: "S3Client",
            access_key: str,
            secret_key: str,
            endpoint_url: str,
    ):
        self.__config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.__session = get_session()

    @asynccontextmanager
    async def __get_client(self):
        async with self.__session.create_client("s3", **self.__config) as client:
            yield client

    async def create_bucket(self, bucket_name: str):
        async with self.__get_client() as client:
            await client.create_bucket(Bucket=bucket_name)

    async def upload_file(self, bucket: str, key: str, file: bytes) -> dict:
        async with self.__get_client() as client:
            return await client.put_object(Bucket=bucket, Key=key, Body=file)

    async def get_file(self, bucket: str, key: str) -> Optional[bytes]:
        async with self.__get_client() as client:
            response = await client.get_object(Bucket=bucket, Key=key)
            async with response['Body'] as stream:
                return await stream.read()

    async def delete_file(self, bucket: str, key: str) -> dict:
        async with self.__get_client() as client:
            return await client.delete_object(Bucket=bucket, Key=key)


s3_client = S3Client(
    access_key=settings.AWS_ACCESS_KEY_ID,
    secret_key=settings.AWS_SECRET_ACCESS_KEY,
    endpoint_url=settings.s3_endpoint_url,
)
