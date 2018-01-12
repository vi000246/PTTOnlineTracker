# 放置系統設置
import collections

# 使用者登入帳密
loginInfo = dict(
    Account='VSCode',
    Password='abcd1234'
)

# 要紀錄上線時間的PTT帳號  (id,是否發送水球)
targetInfo = collections.namedtuple('targetInfo', 'id isSendWater')
targets =[
    targetInfo(id='digforapples',isSendWater=True)
]

# 發送水球的目標
WaterTarget='vi000246'


if __name__ == '__main__':
    print(targets[0].id)
    print(loginInfo['Account'])