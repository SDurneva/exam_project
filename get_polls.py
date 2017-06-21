import json
import requests
import conf


def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+ method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


def get_allwall():
    posts = []
    item_count = 213
    result = vk_api('wall.get', owner_id='130314', access_token=conf.TOKEN, v='5.63', count=100)
    posts += result["response"]["items"]
    while len(posts) < item_count:
        result = vk_api('wall.get', owner_id='130314', v='5.63', count=100, offset=len(posts))
        posts += result
    return posts


def give(posts):
    f = open('polet.json', 'a', encoding='utf-8')
    f.write(json.dumps(posts, ensure_ascii=False))
    f.close()


def get_polls():
    f = open('polet.json', 'r', encoding='utf-8')
    a = json.loads(f.read())
    ds = []
    for d in a:
        if 'attachments' in d:
            ds.append(d)
        else:
            continue
    lists = []
    for d in ds:
        for key in d:
            if key == 'attachments':
                lists.append(d[key])
            else:
                continue
    poll_atts = []
    for el in lists:
        for d in el:
            if 'poll' in d:
                poll_atts.append(d)
            else:
                continue
    polls = []
    for d in poll_atts:
        for key in d:
            if key == 'poll':
                polls.append(d[key])
            else:
                continue
    return polls

def ready_polls(polls):
    f = open('polls.json', 'a', encoding='utf-8')
    f.write(json.dumps(polls, ensure_ascii=False))
    f.close()


def main():
    ready_polls(get_polls())

if __name__ == '__main__':
    main()