class CloudFrontInfo:
    """Encapsulates Amazon CloudFront operations."""

    def __init__(self, cloudfront_client):
        """
        :param cloudfront_client: A Boto3 CloudFront client
        """
        self.cloudfront_client = cloudfront_client


    def get_distribution(self, distribution_id):
        #distribution_id = input(
        #    "This script updates the comment for a CloudFront distribution.\n"
        #    "Enter a CloudFront distribution ID: "
        #)

        distribution_config_response = self.cloudfront_client.get_distribution_config(
            Id=distribution_id
        )
        return distribution_config_response
        #distribution_config = distribution_config_response["DistributionConfig"]
        #distribution_etag = distribution_config_response["ETag"]
#
        #distribution_config["Comment"] = input(
        #    f"\nThe current comment for distribution {distribution_id} is "
        #    f"'{distribution_config['Comment']}'.\n"
        #    f"Enter a new comment: "
        #)
        #self.cloudfront_client.update_distribution(
        #    DistributionConfig=distribution_config,
        #    Id=distribution_id,
        #    IfMatch=distribution_etag,
        #)
        #print("Done!")



