from tqdm import tqdm
import time



class CloudFrontList:
    """Encapsulates Amazon CloudFront operations."""

    def __init__(self, cloudfront_client):
        """
        :param cloudfront_client: A Boto3 CloudFront client
        """
        self.cloudfront_client = cloudfront_client


    def list_distributions(self):
        result = {}
        distributions = self.cloudfront_client.list_distributions()
        if distributions["DistributionList"]["Quantity"] > 0:
            for distribution in tqdm(distributions["DistributionList"]["Items"]):
                tempResult = {}
                #print(f"Domain: {distribution['DomainName']}")
                distributionId = distribution['Id']
                tempResult["DistributionDomain"] = distribution['DomainName']
                result[distributionId] = tempResult
                #print(f"Distribution Id: {distribution['Id']}")
                #print(
                #    f"Certificate Source: "
                #    f"{distribution['ViewerCertificate']['CertificateSource']}"
                #)
                #if distribution["ViewerCertificate"]["CertificateSource"] == "acm":
                #    print(
                #        f"Certificate: {distribution['ViewerCertificate']['Certificate']}"
                #    )
                #print("")
                time.sleep(0.5)
            return result
        else:
            print("No CloudFront distributions detected.")


