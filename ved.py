import requests
import os


video_url = "https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/79/83/1323548379/1323548379_x1-1-100109.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1718432769&gen=playurlv2&os=coso1bv&oi=1972579509&trid=9dbe688e57ca450983886dc82cc34e96p&mid=0&platform=pc&og=cos&upsig=51b400d3ad5f9cfcae775f65b80573cf&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=1,3&buvid=06EBC921-69A9-9A71-1481-85E2923E1DFA78481infoc&build=0&f=p_0_0&agrr=0&bw=15716&logo=40000000"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer': 'https://www.bilibili.com/bangumi/play/ep691452?from_spmid=666.25.episode.0'  # 替换为实际的Referer
}

# 发送请求获取视频内容
response = requests.get(video_url, headers=headers, stream=True)

# 检查请求是否成功
if response.status_code == 200:
    # 创建保存视频的目录
    video_directory = 'videos'
    os.makedirs(video_directory, exist_ok=True)

    # 保存视频文件
    video_file_path = os.path.join(video_directory, 'video1.mp4')
    with open(video_file_path, 'wb') as video_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                video_file.write(chunk)

    print(f"视频已保存到 {video_file_path}")
else:
    print(f"无法访问视频，HTTP状态码: {response.status_code}")
