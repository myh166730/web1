
'''工作室名字：瀚海工作室
根据地用户：分享后所有人可见
根据地用途：数据收集、兴趣推荐
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区，打赏区
现有模块改进灵感：
原创模块，奥运赛事
原创模块一句话功能介绍：奥运赛事有此皆知'''
import streamlit as st
from PIL import Image
import time
page = st. sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])
def p1():
    with open('暮色回响.mp3','rb')as f:
        mymp3=f .read()
    st.audio(mymp3,format= 'audio/mp3',start_time=0)
    
    st.image('奖牌榜.png')
    st.write('截止8.9日奥运会奖牌榜')
    st.write("巴黎奥运会部分中国冠军")
    st.image('樊振东.png')
    st.write('樊振东，1997年1月22日出生于广东省广州市，中国乒乓球队运动员，效力于广东省乒乓球队、中国国家乒乓球队； 现役军人。2012年2月，进入中国国家乒乓球队。12月，第一次参加乒乓球世青赛，就获得了世青赛男单、混双、男团冠军以及男双亚军。2013年11月，还不满17岁的樊振东在国际乒联巡回赛波兰公开赛上击败周雨，成为乒联巡回赛史上最年轻的男单冠军得主。2014年8月，获得第2届夏季青年奥林匹克运动会乒乓球男单决赛冠军，成为完成了世界青年顶级乒乓球赛的大满贯选手。2018年4月，樊振东首次排名乒乓球男单世界第一，成为乒乓球历史上第19位男单世界第一，也是国乒第11位男单世界第一。2019年10月6日，国际乒联瑞典公开赛男双决赛，樊振东/许昕3-2战胜队友梁靖崑/林高远夺冠。10月13日，2019年国际乒联德国公开赛男单决赛，樊振东战胜队友许昕夺冠。12月1日，4比2击败张本智和，第3次拿到男子世界杯冠军。')
    st.image('全红婵.png')
    st.write('全红婵，2007年3月28日出生于广东湛江，中国国家跳水队女运动员。2018年，全红婵获得广东省跳水锦标赛3项冠军。2019年，全红婵获得广东省跳水锦标赛5项冠军。2020年8月，全红婵获得广东省青少年跳水锦标赛3米跳板和10米跳台单双人等5项冠军1项亚军；10月，全红婵以437.75分夺得2020全国跳水冠军赛暨东京奥运会、世界杯选拔赛女子单人10米跳台冠军。2021年3月，全红婵同获2021年中国跳水明星赛女子单人、双人十米跳台亚军；5月，全红婵以440.85分蝉联2021年全国跳水冠军赛暨东京奥运会选拔赛、全运会跳水资格赛女子单人十米跳台冠军；8月，全红婵以五跳三跳满分总466.2分创女子10米跳台历史最高分纪录夺得2020东京奥运会跳水女子单人10米跳台金牌；9月，全红婵连夺中华人民共和国第十四届运动会跳水女子单人十米跳台金牌、跳水女子团体金牌。 2021年8月，全红婵被共青团中央、全国青联授予"中国青年五四奖章" 。9月，全红婵以运动员身份获表彰"全国体育系统先进工作者和劳动模范" ；同月，中华全国总工会授予全红婵全国五一劳动奖章。 2023年10月3日，在杭州第19届亚运会女子单人10米跳台决赛中，全红婵以438.20的成绩获得金牌。2024年2月，全红婵获得2024年世界游泳锦标赛女子10米台冠军。6月，全红婵搭档陈芋汐获得世界杯总决赛女双10米台冠军。7月31日，在巴黎奥运会跳水女子双人10米台比赛中，中国组合陈芋汐/全红婵夺得金牌。')
    st.image('黄雨婷.png')
    st.write('黄雨婷，2006年9月3日出生于浙江省台州市黄岩区上郑乡，中国女子射击运动员，主攻10米气步枪项目。2022年10月的开罗世锦赛，黄雨婷先在女子10米气步枪项目中夺得亚军，为中国夺得一张巴黎奥运会入场券。之后又在该届世锦赛上夺得10米气步枪混合团体和10米气步枪女子团体冠军。2023年9月24日，在杭州第19届亚运会射击女子10米气步枪团体赛中，黄雨婷与王芝琳、韩佳予组成的中国队夺得金牌。同日，在杭州第19届亚运会射击女子10米气步枪个人赛决赛中，黄雨婷以总分252.7环的成绩打破该项目的亚运会纪录，夺得冠军，并成为该届亚运会的首个双冠王。9月25日，盛李豪、黄雨婷组成的中国队获得杭州第19届亚运会射击混合团体10米气步枪决赛冠军。')
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)
    
    
    st.write('----')
    st.write('你知道吗：奥运会的起源是什么？')
    cb1 = st.checkbox('古希腊人为了和平')
    cb2 = st.checkbox('让更多人运动')
    cb3 = st.checkbox('无意义')
    l = [cb2, cb3]
    if st.button('确认答案'):
        if True in l:
            st.write('非然也')
        else:
            st.write('好厉害！')
def p2():
    st.write(':crown:图片处理工具:cat:')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1: 
            st.image(img)
        with tab2:
            st.image(img_change(img,3,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))


def p3():
    '''我的智能词典'''
    st.write(':trophy:智能词典:trophy:')
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list=f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i]=word_list[i].split('#')
    word_dict={}
    for i in word_list:
        word_dict[i[1]]=[int(i[0]),i[2]]#单词：[计数，中文]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        time_list=f.read().split('\n')
    for i in range(len(time_list)):
        time_list[i]=time_list[i].split('#')

    time_dict={}
    for i in time_list:
        time_dict[int(i[0])]=int(i[1])
    






    
    word=st.text_input('请输入你想查询的单词：')
    
    if word in word_dict:
        st.write(word_dict[word])
        n=word_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in time_dict.items():
                message += str(k)+'#'+str(v)+'\n'
            message = message[:-1]
            f.write(message)
            st.write('查询次数: ',time_dict[n])


        if word=='python':
            st.code('''#恭喜你触发彩蛋，这是一行python代码！
                    print("hello world!")''')
        if word=='winter'or word=='cold':
            st.snow()
        if word=='birthday':
            st.balloons()
            if word=='warn':
                st.warning('警告警告！')
        if word =='error':
            st.error('报错！')
        if word=='information':
            st.info('修改后的图片，可以鼠标右击选择【另存为】')
        if word=='wait':
            with st.spinner('Waiting。。。'):
                time.sleep(3)
            st.success('恭喜你成功啦！')
    if cb:
        st.write('选项被勾选', cb)
    
    
    st.write('----')
    st.write('这个词典怎么样？')
    cb1 = st.checkbox('A很好')
    cb2 = st.checkbox('B选A')
    cb3 = st.checkbox('C选B')
    l = []
    if st.button('确认答案'):
        if True in l:
            st.write('非然也')
        else:
            st.write('谢谢您')


def p4():
    st.write('我的留言区')
    
    
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '陌生人':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '朋友':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['陌生人', '朋友'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
if page== '我的兴趣推荐':
    p1() 
elif page=='我的图片处理工具':
    p2()
elif page=='我的智慧词典':
    p3() 
elif page=='我的留言区':
    p4()







