import requests
import asyncio

async def join_group(**kwargs):

    with open('cookies.txt', 'r', encoding='utf-8') as f:
        x = f.readlines()

        index = 0
        account_cookies = []
        for a in x:
            a.replace('\n', '')
            x[index] = a
            account_cookies.append(a)
            index += 1
        # print(x)

    key = 'YOUR-API-KEY'
    pkey = '63E4117F-E727-42B4-6DAA-C8448E9B137F'
    service_url = 'https://roblox-api.arkoselabs.com'
    group_id = kwargs['group_id']

    for cookie in account_cookies:

        response_id = requests.post(f'https://2captcha.com/in.php?json=1&key={key}&method=funcaptcha&publickey={pkey}&surl={service_url}&pageurl=https://www.roblox.com/groups/{group_id}/RoLogging#!/about')
        response_id = response_id.json()['request']


        print(cookie)
        await asyncio.sleep(15)

        while True:
            response_solve = requests.get(f'https://2captcha.com/res.php?key={key}&action=get&id={response_id}&json=1')
            response_solve = response_solve.json()

            if response_solve['request'] != 'CAPCHA_NOT_READY':
                
                token = response_solve['request']#.split('|')[0]
                break
            
            else:
                await asyncio.sleep(5)
                print('Captcha Not Solved, Please wait...')


        data = {
        "captchaToken": f"{token}",
        "captchaProvider": "PROVIDER_ARKOSE_LABS"
        }

        # cookies = {
        #     '.ROBLOSECURITY': '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_F7D5541788E6A04839C8B8E99D8FC9682F1AE341033886882A4571F2D85204E56DEDC681C5FB4419126A928F26DD96576DB40171C550C215BAD83BD427DFE0672D94A95D1F535002E914DD703B742D15CC3042F70E0D1B66E0EE386A35D68651747D4AD64DD8FE50EB9FECA24286CBFC48FDEC0087D1E3420FBFF2A7EEFE661C158812333E071704CDEDFBD304BEAF9012E138624392904C6CA7C3E9F72852343675F45ED2D4118EF95FAF4D474949138C91928466F4F3B3F371C0707323BB81E07D58D29417330C8767D70FD270BFC81BB69E69B468C418F3ABE5672E1792F5C6E7C552842F154E86F3F56E90EB5F4B93A68A73329488C7B66168F37D5B08FB3A4F3C47AA33965163E33E1FB276A6113998FCA176AF0CDBD027358E56278F8CA111F78B235B39E17EFEC1504F7799E49F834B72'
        # }

        print(cookie.strip())
        cookies = {
            '.ROBLOSECURITY': f'{cookie.strip()}'
        }

        try:
            headers = {'X-CSRF-TOKEN': requests.post(url=f'https://auth.roblox.com/v1/logout', cookies=cookies).headers['x-csrf-token']}

            response = requests.post(url=f'https://groups.roblox.com/v1/groups/{group_id}/users', cookies=cookies, data=data, headers=headers)
        except:
            continue

# asyncio.run(join_group(group_id=451243))