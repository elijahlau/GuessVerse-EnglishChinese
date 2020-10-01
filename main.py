# coding=utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
import sqlite3
import random
import win32com.client
import jieba.posseg as pseg
from kivy.core.window import Window



ChapMaxESV = {
    'Genesis': '50',
    'Exodus': '40',
    'Leviticus': '27',
    'Numbers': '36',
    'Deuteronomy': '34',

    'Joshua': '24',
    'Judges': '21',
    'Ruth': '4',
    '1 Samuel': '31',
    '2 Samuel': '24',
    '1 Kings': '22',
    '2 Kings': '25',
    '1 Chronicles': '29',
    '2 Chronicles': '36',
    'Ezra': '10',
    'Nehemiah': '13',
    'Esther': '10',

    'Job': '42',
    'Psalms': '150',
    'Proverbs': '31',
    'Ecclesiastes': '12',
    'Song of Solomon': '8',

    'Isaiah': '66',
    'Jeremiah': '52',
    'Lamentations': '5',
    'Ezekiel': '48',
    'Daniel': '12',

    'Hosea': '14',
    'Joel': '3',
    'Amos': '9',
    'Obadiah': '1',
    'Jonah': '4',
    'Micah': '7',
    'Nahum': '3',
    'Habakkuk': '3',
    'Zephaniah': '3',
    'Haggai': '2',
    'Zechariah': '14',
    'Malachi': '4',

    'Matthew': '28',
    'Mark': '16',
    'Luke': '24',
    'John': '21',
    'Acts': '28',

    'Romans': '16',
    '1 Corinthians': '16',
    '2 Corinthians': '13',
    'Galatians': '6',
    'Ephesians': '6',
    'Philippians': '4',
    'Colossians': '4',
    '1 Thessalonians': '5',
    '2 Thessalonians': '3',
    '1 Timothy': '6',
    '2 Timothy': '4',
    'Titus': '3',
    'Philemon': '1',

    'Hebrews': '13',
    'James': '5',
    '1 Peter': '5',
    '2 Peter': '3',
    '1 John': '5',
    '2 John': '1',
    '3 John': '1',
    'Jude': '1',
    'Revelation': '22'}
BookDictESV = {
    'Genesis': '1',
    'Exodus': '2',
    'Leviticus': '3',
    'Numbers': '4',
    'Deuteronomy': '5',

    'Joshua': '6',
    'Judges': '7',
    'Ruth': '8',
    '1 Samuel': '9',
    '2 Samuel': '10',
    '1 Kings': '11',
    '2 Kings': '12',
    '1 Chronicles': '13',
    '2 Chronicles': '14',
    'Ezra': '15',
    'Nehemiah': '16',
    'Esther': '17',

    'Job': '18',
    'Psalms': '19',
    'Proverbs': '20',
    'Ecclesiastes': '21',
    'Song of Solomon': '22',

    'Isaiah': '23',
    'Jeremiah': '24',
    'Lamentations': '25',
    'Ezekiel': '26',
    'Daniel': '27',

    'Hosea': '28',
    'Joel': '29',
    'Amos': '30',
    'Obadiah': '31',
    'Jonah': '32',
    'Micah': '33',
    'Nahum': '34',
    'Habakkuk': '35',
    'Zephaniah': '36',
    'Haggai': '37',
    'Zechariah': '38',
    'Malachi': '39',

    'Matthew': '40',
    'Mark': '41',
    'Luke': '42',
    'John': '43',
    'Acts': '44',

    'Romans': '45',
    '1 Corinthians': '46',
    '2 Corinthians': '47',
    'Galatians': '48',
    'Ephesians': '49',
    'Philippians': '50',
    'Colossians': '51',
    '1 Thessalonians': '52',
    '2 Thessalonians': '53',
    '1 Timothy': '54',
    '2 Timothy': '55',
    'Titus': '56',
    'Philemon': '57',

    'Hebrews': '58',
    'James': '59',
    '1 Peter': '60',
    '2 Peter': '61',
    '1 John': '62',
    '2 John': '63',
    '3 John': '64',
    'Jude': '65',
    'Revelation': '66'}
BookListESV = [
    'ESV',
    'Genesis',
    'Exodus',
    'Leviticus',
    'Numbers',
    'Deuteronomy',

    'Joshua',
    'Judges',
    'Ruth',
    '1 Samuel',
    '2 Samuel',
    '1 Kings',
    '2 Kings',
    '1 Chronicles',
    '2 Chronicles',
    'Ezra',
    'Nehemiah',
    'Esther',

    'Job',
    'Psalms',
    'Proverbs',
    'Ecclesiastes',
    'Song of Solomon',

    'Isaiah',
    'Jeremiah',
    'Lamentations',
    'Ezekiel',
    'Daniel',

    'Hosea',
    'Joel',
    'Amos',
    'Obadiah',
    'Jonah',
    'Micah',
    'Nahum',
    'Habakkuk',
    'Zephaniah',
    'Haggai',
    'Zechariah',
    'Malachi',

    'Matthew',
    'Mark',
    'Luke',
    'John',
    'Acts',

    'Romans',
    '1 Corinthians',
    '2 Corinthians',
    'Galatians',
    'Ephesians',
    'Philippians',
    'Colossians',
    '1 Thessalonians',
    '2 Thessalonians',
    '1 Timothy',
    '2 Timothy',
    'Titus',
    'Philemon',

    'Hebrews',
    'James',
    '1 Peter',
    '2 Peter',
    '1 John',
    '2 John',
    '3 John',
    'Jude',
    'Revelation']
ChapMaxHHB = {
    '创世记': '50',
    '出埃及记': '40',
    '利未记': '27',
    '民数记': '36',
    '申命记': '34',

    '约书亚记': '24',
    '士师记': '21',
    '路得记': '4',
    '撒母耳记上': '31',
    '撒母耳记下': '24',
    '列王记上': '22',
    '列王记下': '25',
    '历代志上': '29',
    '历代志下': '36',
    '以斯拉记': '10',
    '尼希米记': '13',
    '以斯帖记': '10',

    '约伯记': '42',
    '诗篇': '150',
    '箴言': '31',
    '传道书': '12',
    '雅歌': '8',

    '以赛亚书': '66',
    '耶利米书': '52',
    '耶利米哀歌': '5',
    '以西结书': '48',
    '但以理书': '12',

    '何西阿书': '14',
    '约珥书': '3',
    '阿摩司书': '9',
    '俄巴底亚书': '1',
    '约拿书': '4',
    '弥迦书': '7',
    '那鸿书': '3',
    '哈巴谷书': '3',
    '西番亚书': '3',
    '哈该书': '2',
    '撒迦利亚书': '14',
    '玛拉基书': '4',

    '马太福音': '28',
    '马可福音': '16',
    '路加福音': '24',
    '约翰福音': '21',
    '使徒行传': '28',

    '罗马书': '16',
    '哥林多前书': '16',
    '哥林多后书': '13',
    '加拉太书': '6',
    '以弗所书': '6',
    '腓立比书': '4',
    '歌罗西书': '4',
    '帖撒罗尼迦前书': '5',
    '帖撒罗尼迦后书': '3',
    '提摩太前书': '6',
    '提摩太后书': '4',
    '提多书': '3',
    '腓利门书': '1',

    '希伯来书': '13',
    '雅各书': '5',
    '彼得前书': '5',
    '彼得后书': '3',
    '约翰一书': '5',
    '约翰二书': '1',
    '约翰三书': '1',
    '犹大书': '1',
    '启示录': '22'}
BookDictHHB = {
    '创世记': '1',
    '出埃及记': '2',
    '利未记': '3',
    '民数记': '4',
    '申命记': '5',

    '约书亚记': '6',
    '士师记': '7',
    '路得记': '8',
    '撒母耳记上': '9',
    '撒母耳记下': '10',
    '列王记上': '11',
    '列王记下': '12',
    '历代志上': '13',
    '历代志下': '14',
    '以斯拉记': '15',
    '尼希米记': '16',
    '以斯帖记': '17',

    '约伯记': '18',
    '诗篇': '19',
    '箴言': '20',
    '传道书': '21',
    '雅歌': '22',

    '以赛亚书': '23',
    '耶利米书': '24',
    '耶利米哀歌': '25',
    '以西结书': '26',
    '但以理书': '27',

    '何西阿书': '28',
    '约珥书': '29',
    '阿摩司书': '30',
    '俄巴底亚书': '31',
    '拿鸿书': '32',
    '弥迦书': '33',
    '约拿书': '34',
    '哈巴谷书': '35',
    '西番亚书': '36',
    '哈该书': '37',
    '撒迦利亚书': '38',
    '玛拉基书': '39',

    '马太福音': '40',
    '马可福音': '41',
    '路加福音': '42',
    '约翰福音': '43',
    '使徒行传': '44',

    '罗马书': '45',
    '哥林多前书': '46',
    '哥林多后书': '47',
    '加拉太书': '48',
    '以弗所书': '49',
    '腓立比书': '50',
    '歌罗西书': '51',
    '帖撒罗尼迦前书': '52',
    '帖撒罗尼迦后书': '53',
    '提摩太前书': '54',
    '提摩太后书': '55',
    '提多书': '56',
    '腓利门书': '57',

    '希伯来书': '58',
    '雅各书': '59',
    '彼得前书': '60',
    '彼得后书': '61',
    '约翰一书': '62',
    '约翰二书': '63',
    '约翰三书': '64',
    '犹大书': '65',
    '启示录': '66'}
BookListHHB = [
    "HHB",
    '创世记',
    '出埃及记',
    '利未记',
    '民数记',
    '申命记',

    '约书亚记',
    '士师记',
    '路得记',
    '撒母耳记上',
    '撒母耳记下',
    '列王记上',
    '列王记下',
    '历代志上',
    '历代志下',
    '以斯拉记',
    '尼希米记',
    '以斯帖记',

    '约伯记',
    '诗篇',
    '箴言',
    '传道书',
    '雅歌',

    '以赛亚书',
    '耶利米书',
    '耶利米哀歌',
    '以西结书',
    '但以理书',

    '何西阿书',
    '约珥书',
    '阿摩司书',
    '俄巴底亚书',
    '拿鸿书',
    '弥迦书',
    '约拿书',
    '哈巴谷书',
    '西番亚书',
    '哈该书',
    '撒迦利亚书',
    '玛拉基书',

    '马太福音',
    '马可福音',
    '路加福音',
    '约翰福音',
    '使徒行传',

    '罗马书',
    '哥林多前书',
    '哥林多后书',
    '加拉太书',
    '以弗所书',
    '腓立比书',
    '歌罗西书',
    '帖撒罗尼迦前书',
    '帖撒罗尼迦后书',
    '提摩太前书',
    '提摩太后书',
    '提多书',
    '腓利门书',

    '希伯来书',
    '雅各书',
    '彼得前书',
    '彼得后书',
    '约翰一书',
    '约翰二书',
    '约翰三书',
    '犹大书',
    '启示录']


global QType, QLang, verse, ans1_list, ans2_list, font
font = 0
QType = "随机"
QLang = "English"
mode = "解题"
getans1 = []
getans2 = []
ans1_list = []
ans2_list = []
error1 = "搜索找不到您所指定的章节或字节，又或许需要设置对应的语言"
che = 0
spispeed = 0
verse = "- - -"
speaker = win32com.client.Dispatch('SAPI.SPVOICE')
speaker.Volume = 100
speaker.Rate = spispeed

LabelBase.register('Roboto', 'DroidSansFallback.ttf')
conn = sqlite3.connect('forum.db')
c = conn.cursor()

global bookno, chapno, versno, anschar10, anschar20, anschar30, anschar40, words_list
words_list = "空"

def pick_rand_verse(booksltfn, chapsltfn):
    global myverse, bookno, chapno, versno, VerseID, verse
    verse = "- - -"
    while verse == "- - -":
        conn = sqlite3.connect('forum.db')
        c = conn.cursor()
        if QType == "随机":
            c.execute("SELECT * from VerseTable where bookno=? AND chapno=? ORDER BY Random() LIMIT 1", (booksltfn, chapsltfn,))
        else:
            c.execute("SELECT * from VerseTable where id=? ORDER BY Random() LIMIT 1", (VerseID + 1,))
        myverse = c.fetchone()

        if myverse is None:
            verse = error1
            bookno = 40
            chapno = 0
            versno = 0
        else:
            VerseID = int(myverse[0])
            bookno = int(myverse[1])
            chapno = int(myverse[2])
            versno = int(myverse[3])

            if QLang == "中文":
                verse = str(myverse[4])
            else:
                verse = str(myverse[5])
        print("pick rand verse done, myverse is : ", myverse)
        conn.commit()
    return myverse, verse, bookno, chapno, versno, VerseID

def pick_lookfor_verse(lookforraw):
    global myverse, verse, bookno, chapno, versno
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    lookstr = lookforraw.replace(lookforraw, ("%"+lookforraw+"%"))
    if QLang == "English":
        print("ENG PICK LOOKFOR FUNC lookstr:", lookstr)
        c.execute("SELECT * from VerseTable where VerseESV LIKE ? ORDER BY Random() LIMIT 1", (lookstr,))
        myverse = c.fetchone()
        print("ENG LOOKFOR FUNC  myverse is :", myverse)
        #    print("type of myverse is :", type(myverse))
        if myverse is None:
            verse = error1
            bookno = 40
            chapno = 0
            versno = 0
        else:
            bookno = int(myverse[1])
            chapno = int(myverse[2])
            versno = int(myverse[3])
            verse = str(myverse[5])
    else:
        print("CHI PICK LOOKFOR FUNC lookstr:", lookstr)
        c.execute("SELECT * from VerseTable where Verse LIKE ? ORDER BY Random() LIMIT 1", (lookstr,))
        myverse = c.fetchone()
        print("CHI LOOKFOR FUNC  myverse is :", myverse)
        if myverse is None:
            verse = error1
            bookno = 40
            chapno = 0
            versno = 0
        else:
            #print("type of myverse is :", type(myverse))
            bookno = int(myverse[1])
            chapno = int(myverse[2])
            versno = int(myverse[3])
            verse = str(myverse[4])
    print("pick LOOKFOR verse done, verse is : ", verse)
    conn.commit()
    return myverse, verse, bookno, chapno, versno

def call_book_name(bookno):
    #    global bookno, mybookrow, bookname
    with conn:
        c.execute("SELECT * FROM booklist WHERE Id=?", (bookno,))
    mybookrow = c.fetchone()
    bookname = str(mybookrow[1])
    conn.commit()
    #    print("mybookrow is : ", mybookrow)
    return bookname

def call_book_no(bookname):
    #    global bookno, mybookrow, bookname
    with conn:
        #    conn = sqlite3.connect('forum.db')
        #    c = conn.cursor()
        c.execute("SELECT * FROM booklist WHERE BookName=?", (bookname,))
    mybookrow = c.fetchone()
    print("CALL BOOK NO FUNC mybookrow:", mybookrow)
    #    bookname = mybookrow[1]
    bookno = int(mybookrow[0])
    conn.commit()
    print("bookno is : ", bookno)
    return bookno


def make_qverse(verse, bookname, chapno, versno):
    global ansloc1, words_list, getans1, getans2, ans1_list, ans2_list, ans_word1_loc, ans_word2_loc
    global anschar10, anschar20
    symbol = str('\'!”“"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~“’')
    if verse == error1:
        qverse = error1
        ans1_list = ("x", "x", "x", "x", "x", "x", "x", "x")
        ans2_list = ("x", "x", "x", "x", "x", "x", "x", "x")
        anschar10 = "zz"
        anschar20 = "zz"
    else:
        if QLang == "中文":
            exludes = "的我你他在说人们了是就要和必有这也都为所以从又作与地将使因为儿子去那对不就是上把没有到因行被给事向并之她"
            verse_clean = verse
            for ch in '\'!？！；：”“‘’”"。，、】【#$%&()*+,-./:;<=>?@[\\]^_‘{|}~“’':
                verse_clean = verse_clean.replace(ch, "")

            words = pseg.cut(verse_clean)
            chi_words_list1 = []
            chi_words_list2 = []
            for word, flag in words:

                if word not in exludes:
                    chi_words_list1.append(word)
                    chi_words_list2.append([word, flag])
            print("MQC 1 chi_word_list1 and type is :", chi_words_list1, type(chi_words_list1))
            print("MQC 1 chi_word_list2 and type is :", chi_words_list2, type(chi_words_list2))
            print("chi_words_list1[0] and type", chi_words_list1[0], type(chi_words_list1[0]))
            print("chi_words_list2[0] and type", chi_words_list2[0], type(chi_words_list2[0]))
            if len(chi_words_list1) < 2:
                anslo1 = 0  # answer location of ans_word of the verse
                anslo2 = 1
            else:
                anslo1 = random.randint(0, len(chi_words_list1)-1)
                anslo2 = random.randint(0, len(chi_words_list1)-1)
                while anslo1 == anslo2:
                    anslo2 = random.randint(0, len(chi_words_list1)-1)
            if anslo1 < anslo2:  # make sure anslo1 < anslo2
                pass
            else:
                ans_backup = anslo1
                anslo1 = anslo2
                anslo2 = ans_backup
            conn = sqlite3.connect('dict.db')
            c = conn.cursor()
            print("MQC 2 anslo1, anslo2 is :", anslo1, anslo2) #  from 0 to len(potential_list)
            print("MQC 2  chi_words_list2[anslo1]  chi_words_list2[anslo2] :", chi_words_list2[anslo1], "\n", chi_words_list2[anslo2])

            # c.execute("SELECT Word FROM ChiDict Where WTag=? ORDER BY Random() LIMIT 8 ", (chi_words_list2[anslo1][1],))
            c.execute("SELECT Word FROM ChiDict ORDER BY Random() LIMIT 8")
            getans1 = c.fetchall()
            conn.commit()
            print("MQC 5  getans, chi_words_list2[anslo1][3] is : ", getans1)

            # c.execute("SELECT Word FROM ChiDict Where WTag=? ORDER BY Random() LIMIT 8 ", (chi_words_list2[anslo2][1],))
            c.execute("SELECT Word FROM ChiDict ORDER BY Random() LIMIT 8 ")
            getans2 = c.fetchall()
            conn.commit()
            print("MQC 5 getans, chi_words_list2[anslo2][3] is : ", getans2)
            if len(getans1) != 8:
                c.execute("SELECT Word FROM ChiDict Where WTag=? ORDER BY Random() LIMIT 8 ", ("NOUN",))
                getans1 = c.fetchall()
            if len(getans2) != 8:
                c.execute("SELECT Word FROM ChiDict Where WTag=? ORDER BY Random() LIMIT 8 ", ("NOUN",))
                getans2 = c.fetchall() # 8 words list from dict
            print("MQ6 getans1[1]: ", getans1[0])
            print("MQ6 getans1[0][0]: ", getans1[0][0])
            print("MQ6 type of getans1[0][0]: ", type(getans1[0][0]))

            ans1_list = []
            ans2_list = []
            ans_word1_loc = random.randint(1, 8) # includes 1 and 8
            ans_word2_loc = random.randint(1, 8)
            print("MQC 6 ans_word1_loc, ans_word2_loc", ans_word1_loc, ans_word2_loc)

            for i in range(1, 9):
                ans1_list.append(getans1[i-1][0])  # make list from 8 words
            ans1_list.insert(ans_word1_loc-1, chi_words_list2[anslo1][0])  # insert answer into (ans_word1_loc -1) among 8 words
            for i in range(1, 9):
                ans2_list.append(getans2[i-1][0])
            ans2_list.insert(ans_word2_loc-1, chi_words_list2[anslo2][0])
            print("MQC 9 ans1_list, ans2_list : ", ans1_list,  ans2_list)

            selword1 = ans1_list[ans_word1_loc-1]
            selword2 = ans2_list[ans_word2_loc-1]
            anschar10 = selword1
            anschar20 = selword2
            print("MQC 9.5 selword1 and selword2 : ", selword1, selword2)
            qverse_raw = verse.replace(selword1, "_____", )
            qverse_raw = qverse_raw.replace(selword2, "_____", )
            print("MQC 10 qverse_raw :", qverse_raw)
            qverse = "《" + bookname + str(chapno) + "章" + str(versno) + "节》\n " + qverse_raw
            print("MQC 10 make qverse func : qverse is   ", qverse)



        else: ### ENGLISH~!~!~!~!~!
            verse_clean = verse
            for ch in '\'!”"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~“’':
                verse_clean = verse_clean.replace(ch, " ")
            # words_list = nltk.word_tokenize(text=verse_clean)
            verse_clean = verse_clean.strip("\n").split(" ")
            words_list = []
            for w in verse_clean:
                if w != "":
                    words_list.append(w)
            print("words list is :", words_list)
            print("words_list length", len(words_list))
            conn = sqlite3.connect('dict.db')
            c = conn.cursor()
            potential_list = []
            b = 0
            for i in words_list:
                b = b + 1
                # print("MQE 1.1 i.lower() is :", i.lower())
                c.execute("SELECT * FROM EngDict WHERE Word=?", (i.lower(),))
                getdict = c.fetchone()
                # print("MQE 1.2 getdict is :", getdict)
                if getdict is None:
                    getdict = [99999, i, 'INS', 99999]
                # print(getdict)
                freq = int(getdict[3])
                if freq < 2000:
                    potential_list.append((b, i, freq, getdict[2]))
                # print("MQE 1.3 DICT : ", i, ",  ", freq)
            print("MQE1 potential_list : ", potential_list)
            print("MQE2 Length of potential_list : ", len(potential_list))
            # conn.close()

            if len(potential_list) < 2:
                anslo1 = 0  # answer location of ans_word of the verse
                anslo2 = 1
            else:
                anslo1 = random.randint(0, len(potential_list)-1)
                anslo2 = random.randint(0, len(potential_list)-1)
                while anslo1 == anslo2:
                    anslo2 = random.randint(0, len(potential_list)-1)

            if anslo1 < anslo2:  # make sure anslo1 < anslo2
                pass
            else:
                ans_backup = anslo1
                anslo1 = anslo2
                anslo2 = ans_backup
            print("MQE3 anslo1, anslo2 is :", anslo1, anslo2) #  from 0 to len(potential_list)
            print("MQE4 potential_list[anslo1]  potential_list[anslo2] :", potential_list[anslo1],"\n" , potential_list[anslo2])

            c.execute("SELECT Word FROM EngDict Where WTag=? ORDER BY Random() LIMIT 8 ", (potential_list[anslo1][3],))
            getans1 = c.fetchall()
            conn.commit()
            print("MQE5 getans, potential_list[anslo1][3] is : ", getans1, potential_list[anslo1][3])

            c.execute("SELECT Word FROM EngDict Where WTag=? ORDER BY Random() LIMIT 8 ", (potential_list[anslo2][3],))
            getans2 = c.fetchall()
            conn.commit()
            print("MQE5 getans, potential_list[anslo2][3] is : ", getans2, potential_list[anslo2][3])
            #     c.execute("CREATE TABLE EngDict (Id int, Word VARCHAR(30), WTag VARCHAR(10), WCount int, Meaning text)")
            if len(getans1) != 8:
                c.execute("SELECT Word FROM EngDict Where WTag=? ORDER BY Random() LIMIT 8 ", ("NOUN",))
                getans1 = c.fetchall()
            if len(getans2) != 8:
                c.execute("SELECT Word FROM EngDict Where WTag=? ORDER BY Random() LIMIT 8 ", ("NOUN",))
                getans2 = c.fetchall() # 8 words list from dict
            print("MQ6 getans1[1]: ", getans1[0])
            print("MQ6 getans1[0][0]: ", getans1[0][0])
            print("MQ6 type of getans1[0][0]: ", type(getans1[0][0]))

            ans1_list = []
            ans2_list = []
            ans_word1_loc = random.randint(1, 8) # includes 1 and 8
            ans_word2_loc = random.randint(1, 8)
            print("MQE6 ans_word1_loc, ans_word2_loc", ans_word1_loc, ans_word2_loc)

            for i in range(1, 9):
                ans1_list.append(getans1[i-1][0])  # make list from 8 words
            ans1_list.insert(ans_word1_loc-1, potential_list[anslo1][1])  # insert answer into (ans_word1_loc -1) among 8 words
            for i in range(1, 9):
                ans2_list.append(getans2[i-1][0])
            ans2_list.insert(ans_word2_loc-1, potential_list[anslo2][1])

            print("MQE9 ans1_list, ans2_list : ", ans1_list,  ans2_list)
            selword1 = ans1_list[ans_word1_loc-1]
            selword2 = ans2_list[ans_word2_loc-1]
            anschar10 = selword1
            anschar20 = selword2
            print("MQE 9.5 selword1 and selword2 : ", selword1, selword2)
            qverse_raw = verse.replace(selword1, "_____", )
            qverse_raw = qverse_raw.replace(selword2, "_____", )
            print("MQE 10 qverse_raw :", qverse_raw)
            qverse = "《" + bookname + str(chapno) + "章" + str(versno) + "节》\n " + qverse_raw
            print("MQE 10 make qverse func : qverse is   ", qverse)
            ansloc1 = 1
    return qverse, ansloc1

defaultbook = "马太福音"
booksltfn = 40
if ChapMaxHHB[defaultbook] == 1:
    chapsltfn = 1
else:
    chapsltfn = random.randint(1, int(ChapMaxHHB[defaultbook]))
print("001 MAIN ChapMaxHHB(defaultbook) and chapsltfn : ", ChapMaxHHB[defaultbook], chapsltfn)

bookname = call_book_name(booksltfn)
pick_rand_verse(booksltfn, chapsltfn)  # return myverse, verse, bookno, chapno, versno


qverse_ansloc1 = make_qverse(verse, bookname, chapno, versno)  # return qverse, ansloc1
qverse = qverse_ansloc1[0]
ansloc1 = qverse_ansloc1[1]
# qverse_raw = verse.replace(verse[ansloc1:ansloc1 + 4], "__ __ __ __", 1)
# qverse = "《" + bookname + str(chapno) + "章" + str(versno) + "节》\n " + qverse_raw
oriverse = "《" + bookname + str(chapno) + "章" + str(versno) + "节》\n " + verse
answer = "答案"

global slt1, slt2, slt3, slt4
slt1 = 0
slt2 = 0

ansclick = 0
runnum = -1

messagelist = [
    "可选：《随机》出题，或者按着顺序用当前的经文的《下一节》出题。 ",
    "可选：《中文》或英文《English》 ",
    "可选：语音播放《速度》，《+》的更快，《-》 的更慢。",
    "可选：《解题》模式或《学习》模式 ",
    "可选：《字体》大小可以选择 ",
    "可以查英文字典： 点击《英文词典》，选择词条，点击《显示词典》",
    "可以从显示词典返回显示经文：点击同一个按钮，点击《显示经文》",
    "如果《绿色格子》已经有英文字，可以点击格子可以显示英文意思",
    "点击《读出》可以朗读主屏内容",
    "要更了解如何使用，请点击《再来一题》按钮",
    "您不需要用鼠标次键（一般上右键是次键）",
    "需要填入两个词，有16个答案选项",
    "第一列和第二列的八个词对应第一的答案。第三和第四列的词是第二的答案",
    "如果没有选择特定书本，这程序默认只从《马太福音》提取经文做填充题",
    "点击程序顶部的按钮，可以改变经文提取范围",
    "点击《摩西五经》，点击《全选》，程序就会从这五本书提取经文",
    "想取消已经选择的书，就点击《不选》",
    "如果要从正本圣经随机提取经文，八个按钮都点击[全选]",
    "有时候，书的列表选项太长，可以用鼠标滚轮",
    "你可以缩小某书的经文提取范围，而不是整本书",
    "可以在《从几章》和《到几章》的格子填入数字",
    "如果只是要从一章里面提取经文，两个格子都填同一个数",
    "两个绿色格子是答案栏，它们会显示您的选择",
    "通过《指定字节》可以缩小经文提取范围，仅选择有这关键词的经文",
    "看不到输入法选项的，需要从其他文本复制，然后粘贴进来《指定字节》，或者盲输入",
    "《指定字节》中可以填写 \"耶稣\" ，不包括 \" 符号，程序会选择有 \" 耶稣 \" 的经文",
    "《指定字节》中有输入文字的时候，限制书的范围是无效的",
    "不要在《指定字节》中输入空格",
    "欢迎反馈：wall-building@hotmail.com",
    "愿上帝赐福您 -- 来自《所罗门与小花》微信公众号"]

class MyGrid(Widget):
    global slt1, slt2, slt3, slt4, chapno, bookno, versno, bookname, qrand, qnext, QLang, che
    ans1 = ObjectProperty(None)
    ans2 = ObjectProperty(None)
    ans3 = ObjectProperty(None)
    ans4 = ObjectProperty(None)
    inst = ObjectProperty(None)
    rev = ObjectProperty(None)
    #qverse = ObjectProperty(None)
    words_list = ObjectProperty(None)
    #qverse = qverse
    answer = answer

    che = 0
    def check(self):
        global che
        if che == 0:
            word = self.dict.text
            conn = sqlite3.connect('dict.db')
            c = conn.cursor()
            c.execute("SELECT * FROM EngDict WHERE Word=?", (word.lower(),))
            result = c.fetchone()
            if result == None:
                getdict ="请选择要查的英文词。或查找不到。"
            else:
                getdict = result[4]
                getdict = getdict.replace("Ȁ", "; ")
                getdict = getdict.replace("：(", "： (")
                getdict = getdict.replace(";(", "; (")
                getdict = getdict.replace("；(", "； (")
                getdict = getdict.replace(":(", ": (")
            for i in "只限英文":
                if word == i:
                    self.qverse.text = "只限英文词典"
                    break
                else:
                    self.qverse.text = word + ":  " + getdict
            che = 1
            self.gcheck.text = "显示经文"
        else:
            self.qverse.text = qverse
            self.gcheck.text = "显示词典"
            che = 0

    def voice(self):
        content = self.qverse.text
        if content[0] == "《":
            content = content.split("》", 1)
            content = content[1]
        if self.spispd.text == "正常":
            spispeed = 0
        else:
            spispeed = int(self.spispd.text)
        content = content.replace("_____", ",")
        speaker.Rate = spispeed
        speaker.Speak(content)

    def ques(self):
        voice = qverse.split("\n", 2)
        speech = voice[1].replace("__", ",", 2)
        speaker.Speak(speech)

    def say(self, word):
        speaker.Speak(word)

    def font_c(self):
        global font_inc, font_disp
        if self.font.text == "原设定":
            font_inc = 0
        else:
            font_inc = int(self.font.text)
        font_disp = font_inc + 24
        print("FONT_C: font_disp AND font_inc is : ", font_disp, font_inc)
        self.qverse.font_size = font_disp
        self.but1.font_size = font_disp
        self.but2.font_size = font_disp
        self.but3.font_size = font_disp
        self.but4.font_size = font_disp
        self.but5.font_size = font_disp
        self.but6.font_size = font_disp
        self.but7.font_size = font_disp
        self.but8.font_size = font_disp
        self.but11.font_size = font_disp
        self.but12.font_size = font_disp
        self.but13.font_size = font_disp
        self.but14.font_size = font_disp
        self.but15.font_size = font_disp
        self.but16.font_size = font_disp
        self.but17.font_size = font_disp
        self.but18.font_size = font_disp
        self.ans1.font_size = font_disp
        self.ans2.font_size = font_disp
                # ("原设定", "+2", "+4", "+6", "+8", "+10", "+12", "+14", "+16", "+18")

    def restart(self):
        global verse, bookno, bookname, qverse, ansind10, ansind20, ansind30, ansind40, QType, QLang, mode
        global ansclick, booksltfn, ansloc1, slt1, slt2, runnum, oriverse, words_list, ans1_list, ans2_list
        booksltfn = 40
        ansclick = 0
        bookslt1 = []
        MyFont = self.font.text
        QType = self.spiq.text
        print("QType is : ", QType)
        QLang = self.spil.text
        spilang = QLang #中文,英文, 中英文
        spispeedbackup = self.spispd.text
        if self.spimode.text == "学习":
            mode = "学习"
        else:
            mode = "解题"

        # if self.font.text == "原设定":
        #     font_inc = 0
        # else:
        #     font_inc = self.font.text



        if self.spi1.text == '(不选)':
            self.spi1.text = '摩西五经'
            self.spi1.outline_color = (0.1, 0.1, 0.1)
        elif self.spi1.text == '摩西五经':
            pass
        elif self.spi1.text == '(全选)':
            self.spi1.text = '(全选)'
            bookslt1 = [1, 2, 3, 4, 5]
            self.spi1.outline_color = (0, 0, 1)
        else:
            self.spi1.outline_color = (0, 0.3, 0)
            print("-001 RESTART FUNC  MyApp.spi1.spi1txt", self.spi1.text)
            spi1 = self.spi1.text
            bookslt1 = [BookDictHHB[spi1]]
        print("000 RESTART FUNC MyApp.spi1   :", self.spi1)
        print("000 RESTART FUNC MyApp.spi1.spi1txt   :", self.spi1.text)
        spislt1 = self.spi1.text

        bookslt2= []
        if self.spi2.text == '(不选)':
            self.spi2.text = '历史书'
        elif self.spi2.text == '历史书':
            pass
        elif self.spi2.text == '(全选)':
            bookslt2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            self.spi2.outline_color = (0.0, 0.5, 0.5, 1)
        else:
            self.spi2.outline_color = (0.0, 0.5, 0.5, 1)
            spi2 = self.spi2.text
            print("spi2 is : ", spi2)
            print("-01 RESTART FUNC  MyApp.spi2.spi2txt", self.spi2.text)
            bookslt2 = [BookDictHHB[spi2]]
        spislt2 = self.spi2.text

        bookslt3= []
        if self.spi3.text == '(不选)':
            self.spi3.text = '诗歌智慧'
        elif self.spi3.text == '诗歌智慧':
            pass
        elif self.spi3.text == '(全选)':
            bookslt3 = [18, 19, 20, 21, 22]
        else:
            spi3 = self.spi3.text
            print("spi3 is : ", spi3)
            bookslt3 = [BookDictHHB[spi3]]
        spislt3 = self.spi3.text

        bookslt4= []
        if self.spi4.text == '(不选)':
            self.spi4.text = '大先知书'
        elif self.spi4.text == '大先知书':
            pass
        elif self.spi4.text == '(全选)':
            bookslt4 = [23, 24, 25, 26, 27]
        else:
            spi4 = self.spi4.text
            print("spi4 is : ", spi4)
            bookslt4 = [BookDictHHB[spi4]]
        spislt4 = self.spi4.text


        bookslt5= []
        if self.spi5.text == '(不选)':
            self.spi5.text = '小先知书'
        elif self.spi5.text == '小先知书':
            pass
        elif self.spi5.text == '(全选)':
            bookslt5 = [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        else:
            spi5 = self.spi5.text
            print("spi5 is : ", spi5)
            bookslt5 = [BookDictHHB[spi5]]
        spislt5 = self.spi5.text

        bookslt6 = []
        if self.spi6.text == '(不选)':
            self.spi6.text = '福音.历史'
        elif self.spi6.text == '福音.历史':
            pass
        elif self.spi6.text == '(全选)':
            bookslt6 = [40, 41, 42, 43, 44]
        else:
            spi6 = self.spi6.text
            print("spi6 is : ", spi6)
            bookslt6 = [BookDictHHB[spi6]]
        spislt6 = self.spi6.text

        bookslt7 = []
        if self.spi7.text == '(不选)':
            self.spi7.text = '保罗书信'
        elif self.spi7.text == '保罗书信':
            pass
        elif self.spi7.text == '(全选)':
            bookslt7 = [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        else:
            spi7 = self.spi7.text
            print("spi7 is : ", spi7)
            bookslt7 = [BookDictHHB[spi7]]
        spislt7 = self.spi7.text

        bookslt8 = []
        if self.spi8.text == '(不选)':
            self.spi8.text = '其他启示'
        elif self.spi8.text == '其他启示':
            pass
        elif self.spi8.text == '(全选)':
            bookslt8 = [58, 59, 60, 61, 62, 63, 64, 65, 66]
        else:
            spi8 = self.spi8.text
            print("spi8 is : ", spi8)
            bookslt8 = [BookDictHHB[spi8]]
        spislt8 = self.spi8.text

        print("bookslt1234 is : ", bookslt1, bookslt2, bookslt3)
        bookcho = []
        bookcho = bookslt1 + bookslt2 + bookslt3 + bookslt4 + bookslt5 + bookslt6 + bookslt7 + bookslt8
        print("booklist is : ", bookcho)
        random.shuffle(bookcho)
        if len(bookcho)== 0:
            booksltfn = 40
        else:
            booksltfn = int(bookcho[0])
        # print("0 RESTART FUNC  booksltfn:", booksltfn)
        # print("00 RESTART CHAP self.chapstart.text", self.chapstart.text)
        bookname = call_book_name(booksltfn)
        # print("***00 RESTART FUNC Bookname : ", bookname)
        chapstartraw = self.chapstart.text
        chapendraw = self.chapend.text
        if ((chapstartraw == "") or (chapendraw == "")) and ChapMaxHHB[bookname] != 1:
            chapsltfn = random.randint(1, int(ChapMaxHHB[bookname]))
            print("010 RESTART FUNC chapsltfn chapsltfn chapsltfn", chapsltfn)
            chapstartraw = ""
            chapendraw = ""
        else:
            chapstartint = int(chapstartraw)
            chapendint = int(chapendraw)
            if chapstartint == chapendint:
                chapsltfn = chapstartint
            else:
                chapsltfn = random.randint(chapstartint, chapendint)

        lookforraw = self.lookfor.text

        self.clear_widgets()

        # reset verse, if LOOKFOR is TRUE, priority to use LOOKFOR
        verse = "-"
        while verse == "-":
            if lookforraw != "":  # if LOOKFOR is True
                resultlk = pick_lookfor_verse(lookforraw) # return myverse, verse, bookno, chapno, versno
                verse = resultlk[1]
                bookno = resultlk[2]
                chapno = resultlk[3]
                versno = resultlk[4]
                bookname = call_book_name(bookno)
                print("RESTART FUNC WHILE LOOK looforraw :", lookforraw)
                print("RESTART FUNC WHILE LOOK resultlk :", resultlk)
            else:  # if LOOKFOR is FALSE
                result = pick_rand_verse(booksltfn, chapsltfn)
                verse = result[1]  # return myverse, verse, bookno, chapno, versno
                print("result", result)
                bookno = result[2]
                chapno = result[3]
                versno = result[4]
                print("RESTART FUNC WHILE ELSE booksltfn :", booksltfn)
                print("RESTART FUNC WHILE ELSE chapsltfn :", chapsltfn)
                bookname = call_book_name(bookno)


        print("2 restart func verse", verse)
        qverse_ansloc1 = make_qverse(verse, bookname, chapno, versno)  # return qverse, ansloc1
        qverse = qverse_ansloc1[0]
        ansloc1 = qverse_ansloc1[1]

        verse_clean = verse
        for ch in '\'!”"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~“’':
            verse_clean = verse_clean.replace(ch, " ")
        #    words_list = verse_clean.split(" ")
        if QLang == "English":
            verse_clean = verse_clean.strip("\n").split(" ")
            words_list = []
            for w in verse_clean:
                if w != "":
                    words_list.append(w)
        else:
            words_list = "只限英文"
        if mode == "学习":
            MyApp.qverse = "《" + bookname + str(chapno) + "章" + str(versno) + "节》\n " + verse
        else:
            MyApp.qverse = qverse

        MyApp.words_list = words_list
        print("words_list", words_list)
        MyApp.chapstart = chapstartraw
        MyApp.chapend = chapendraw
        MyApp.lookfor = lookforraw
        MyApp.spiq = QType
        MyApp.spil = spilang
        MyApp.spispd = spispeedbackup
        MyApp.spimode = mode
        MyApp.font = MyFont

        MyApp.spi1 = spislt1
        MyApp.spi2 = spislt2
        MyApp.spi3 = spislt3
        MyApp.spi4 = spislt4
        MyApp.spi5 = spislt5
        MyApp.spi6 = spislt6
        MyApp.spi7 = spislt7
        MyApp.spi8 = spislt8

        MyApp.btn1 = ans1_list[0]
        MyApp.btn2 = ans1_list[1]
        MyApp.btn3 = ans1_list[2]
        MyApp.btn4 = ans1_list[3]
        MyApp.btn5 = ans1_list[4]
        MyApp.btn6 = ans1_list[5]
        MyApp.btn7 = ans1_list[6]
        MyApp.btn8 = ans1_list[7]


        MyApp.btn11 = ans2_list[0]
        MyApp.btn12 = ans2_list[1]
        MyApp.btn13 = ans2_list[2]
        MyApp.btn14 = ans2_list[3]
        MyApp.btn15 = ans2_list[4]
        MyApp.btn16 = ans2_list[5]
        MyApp.btn17 = ans2_list[6]
        MyApp.btn18 = ans2_list[7]

        runnum = (runnum + 1) % 30
        MyApp.inst = messagelist[runnum]
        slt1 = 0
        slt2 = 0

        self.parent.add_widget(MyGrid())

        # self.font_c()
        # self.qverse.font_size = 40
        # self.qverse.text = str(50)
        # print("6 restart func. AFTER BUILD, MyApp.spi1", MyApp.spi1)
        # print("----------------------------------------------------------------")
        return booksltfn, ansclick, slt1, slt2





    def rev(self):
        global ansclick, anschar1234
        ansclick = ansclick + 1
        if ansclick == 1:
            anschar1234 = anschar10
        elif ansclick > 1:
            anschar1234 = anschar10 + "    " + anschar20
        self.inst.text = anschar1234
        # self.inst.outline_color = (0, 0, 0.7)
        # self.inst.outline_width = 2

    def submit(self):
        global slt1, slt2, ans_word1_loc, ans_word2_loc

        print("SUBMIT func: slt 1,2:   ", slt1, slt2)
        if ((slt1 == ans_word1_loc) + (slt2 == ans_word2_loc))  == 2:
            self.inst.text = "哇！答对了！"
            self.inst.outline_color = (0.7, 0, 0)
            self.inst.outline_width = 2
        elif ((slt1 == ans_word1_loc) + (slt2 == ans_word2_loc))  == 1 :
            self.inst.text = "对了一个！"
        else:
            self.inst.text = "太惨了………全错了！"

    def btn1(self):
        global slt1
        slt1 = 1
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])

    def btn2(self):
        global slt1
        slt1 = 2
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])

    def btn3(self):
        global slt1
        slt1 = 3
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])

    def btn4(self):
        global slt1
        slt1 = 4
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])

    def btn5(self):
        global slt1
        slt1 = 5
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])

    def btn6(self):
        global slt1
        slt1 = 6
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])
    def btn7(self):
        global slt1
        slt1 = 7
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])
    def btn8(self):
        global slt1
        slt1 = 8
        self.ans1.text = ans1_list[slt1 - 1]
        self.say(ans1_list[slt1 - 1])


    def btn11(self):
        global slt2
        slt2 = 1
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])
    def btn12(self):
        global slt2
        slt2 = 2
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])
    def btn13(self):
        global slt2
        slt2 = 3
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])
    def btn14(self):
        global slt2
        slt2 = 4
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])
    def btn15(self):
        global slt2
        slt2 = 5
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])
    def btn16(self):
        global slt2
        slt2 = 6
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])
    def btn17(self):
        global slt2
        slt2 = 7
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])
    def btn18(self):
        global slt2
        slt2 = 8
        self.ans2.text = ans2_list[slt2 - 1]
        self.say(ans2_list[slt2 - 1])

    def ansc1(self):
        global slt1, che
        # print("Name: ", self.ans1.text)
        # self.ans1.text = ""
        slt1 = 0
        che = 0
        if che == 0:
            word = self.ans1.text
            conn = sqlite3.connect('dict.db')
            c = conn.cursor()
            c.execute("SELECT * FROM EngDict WHERE Word=?", (word.lower(),))
            result = c.fetchone()
            if result == None:
                getdict = "请选择要查的英文词。或查找不到。"
            else:
                getdict = result[4].replace("Ȁ", "; ")
                getdict = getdict.replace("：(", "： (")
                getdict = getdict.replace(";(", "; (")
                getdict = getdict.replace("；(", "； (")
                getdict = getdict.replace(":(", ": (")
            for i in "只限英文":
                if word == i:
                    self.qverse.text = "只限英文词典"
                    break
                else:
                    self.qverse.text = word + ":  " + getdict
            che = 1
            self.gcheck.text = "显示经文"
        else:
            self.qverse.text = qverse
            self.gcheck.text = "显示词典"
            che = 0

    def ansc2(self):
        global slt2, che
        # print("Name: ", self.ans1.text)
        # self.ans2.text = ""
        slt2 = 0
        che = 0
        if che == 0:
            word = self.ans2.text
            conn = sqlite3.connect('dict.db')
            c = conn.cursor()
            c.execute("SELECT * FROM EngDict WHERE Word=?", (word.lower(),))
            result = c.fetchone()
            if result == None:
                getdict = "请选择要查的英文词。或查找不到。"
            else:
                getdict = result[4]
                getdict = getdict.replace("Ȁ", "; ")
                getdict = getdict.replace("：(", "： (")
                getdict = getdict.replace(";(", "; (")
                getdict = getdict.replace("；(", "； (")
                getdict = getdict.replace(":(", ": (")
            for i in "只限英文":
                if word == i:
                    self.qverse.text = "只限英文词典"
                    break
                else:
                    self.qverse.text = word + ":  " + getdict
            che = 1
            self.gcheck.text = "显示经文"
        else:
            self.qverse.text = qverse
            self.gcheck.text = "显示词典"
            che = 0


class MyApp(App):
    #    global qverse
    font = str("原设定")
    chapstart = str("")
    chapend = str("")
    lookfor = str("")
    qverse = qverse
    words_list = words_list
    spiq = str("随机")
    spil = str("English")
    spispd = str("正常")
    spimode = str("解题")
    gcheck = str("显示词典")
    submit = str("提交")
    title = str("中英圣经填充")
    restart = str("再来一节")
    rev = str("提示答案")
    inst = str("第一次使用，可以连续点击《再来一节》看提示")
    spi1 = str("摩西五经")
    spi2 = str("历史书")
    spi3 = str("诗歌智慧")
    spi4 = str("大先知书")
    spi5 = str("小先知书")
    spi6 = str("福音.历史")
    spi7 = str("保罗书信")
    spi8 = str("其他启示")

    btn1 = ans1_list[0]
    btn2 = ans1_list[1]
    btn3 = ans1_list[2]
    btn4 = ans1_list[3]
    btn5 = ans1_list[4]
    btn6 = ans1_list[5]
    btn7 = ans1_list[6]
    btn8 = ans1_list[7]

    btn11 = ans2_list[0]
    btn12 = ans2_list[1]
    btn13 = ans2_list[2]
    btn14 = ans2_list[3]
    btn15 = ans2_list[4]
    btn16 = ans2_list[5]
    btn17 = ans2_list[6]
    btn18 = ans2_list[7]

    def build(self):

        return MyGrid()


if __name__ == "__main__":
    #Config.set('graphics', 'resizable', False)
    Window.size = (1024, 768)
    MyApp().run()

