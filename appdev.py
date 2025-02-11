import boto3
import time
from tools.tool_cloudFrontList import CloudFrontList
from tools.tool_cloudFrontInfo import CloudFrontInfo
from tools.tool_telegram import telegramBotTools

# ENV
import os
LOOP_INTERVAL = os.getenv(key="LOOP_INTERVAL")




cf_client = boto3.client('cloudfront')
bot = telegramBotTools()

def cloudFrontStatus():
    result = ["☁️ * AWS Cloudfront Status * \n\n"]
    cfl = CloudFrontList(cf_client)
    distributions = cfl.list_distributions()
    distribution_ids = distributions.keys()
    cfi = CloudFrontInfo(cf_client)
    for id in distribution_ids :
        distribution_info = cfi.get_distribution(id)
        distribution_Alias = distribution_info['DistributionConfig']['Aliases']['Items'][0]
        # check domain is wiimage.com
        if not (distribution_Alias.split('.')[-1] == "com" and distribution_Alias.split('.')[-2] == "wiimage") :
            continue
        distribution_Http_Status = distribution_info['ResponseMetadata']['HTTPStatusCode']
        distribution_Status = distribution_info['DistributionConfig']['Enabled']
        if distribution_Http_Status == 200 and distribution_Status == True :
            #result.append(f"🟢 {distribution_Alias}\n")
            pass
        else :
            result.append(f"🔴 {distribution_Alias}\n")
    return result

async def app():
    while True :
        cloudfrontstatus = cloudFrontStatus()
        if len(cloudfrontstatus) > 1 :
            msg = ''.join(str(x) for x in cloudfrontstatus)
            await bot.sendMessage(msg)
        time.sleep(int(LOOP_INTERVAL))

if __name__ == "__main__" :
    import asyncio
    asyncio.run(app())