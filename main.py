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