import requests
from operator import itemgetter

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

def calc_age(uid):
    req = "https://api.vk.com/method/users.get?v=5.81&access_token="+ACCESS_TOKEN+"&user_ids="+uid
    r_user = requests.get(req)
    user_id = r_user.json()["response"][0]["id"]
    print("user_id is ", user_id)
    req2 = "https://api.vk.com/method/friends.get?v=5.81&access_token="+ACCESS_TOKEN+"&user_id="+str(user_id)+"&fields=bdate"
    r_friends = requests.get(req2)
    print(r_friends)

    friends = r_friends.json()["response"]["items"]
    ages = []
    for i in friends:
        if 'bdate' in i and len(i["bdate"])>6:
            ages.append(2022-int(i["bdate"][-4:]))
    count_age = []
    uq_age = []
    for i in ages:
        if i not in uq_age:
            uq_age.append(i)
            count_age.append((i, ages.count(i)))

    count_age = sorted(sorted(count_age, key=itemgetter(0)),key=itemgetter(1), reverse = True)
    return count_age

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
