

#수강신청 프로그램 (1. 회원가입 - 2. 로그인 - 3. 개인정보입력 - 4. 수강신청 - 5. 수강정보관리)
cnt=0
while(1):

    #회원가입 시스템
    a = ["1234"]  # 아이디 리스트 생성
    b = ["1234"]  # 비번 리스트 생성
    c = input("회원가입하시겠습니까?y/n")
    if c == "y":

        menu1= input("아이디를 입력해주세요")

        a.append(menu1) #생성된 리스트에 아이디 추가

        d = input("비밀번호를 입력해주세요")

        b.append(d)  #생성된 리스트에 비번 추가
        print("**********************")
        print("회원가입이 완료 되었습니다")
        print("***************")
        print("다시로그인해주세요")
        print("***************")
        #로그인 시스템
        id = input('ID 입력:')
        pw = input('PW 입력:')

        if id in a and pw in b:
            print('로그인 성공')

        elif cnt>=5:
            print("로그인에 5회 실패하셨습니다")
            break
        else:
            cnt = cnt + 1
            print('로그인  실패'.format(cnt))
            break


    #기존 회원( 회원가입이 되있는 상태에서)
    else:
        id = input('ID 입력:')
        pw = input('PW 입력:')

        if id in a and pw in b:
            print('로그인 성공')
        elif cnt>=5:
            break

        else:
            cnt = cnt + 1
            print('로그인 {}회 실패'.format(cnt))
            break
    #개인정보 등록
    print("수강신청을 하기위해 개인정보를 입력해주세요")
    name = input("이름을 입력하세요. ")
    age = input("나이를 입력하세요. ")
    major = input("전공을 입력하세요.")
    class1=input("학번을 입력하세요")


    #조건문을 사용한 수강신청 프로그램
    #실제 수강신척 목록 참조
    #코드가 너무 길어져 (교양:사고와 표현.,msc:프로그래밍,공학물리)만 수강신청 과목으로 선정함
    while(2):
        print(" ==== 수강신청 프로그램 ====")
        subject = int(input("1.교양과목 신청 2.MSC 과목 신청 3.수강생 정보관리  4. 종료 "))
        if subject == 1:
            ky = int(input("1. 사고와표현 " ))
            if ky == 1:
                time = int(input("1.월123  2.월789  3.화678 "))
                if time == 1:
                    dict1 = {"0091": "조극훈", "0092": "김문희", "0093": "김화경", "0094": "최준호", "0095": "윤대선"}#딕셔너리로 코드와 교수 저장
                    dict2 = {"조극훈": 49, "김문희": 16, "김화경": 17, "최준호": 18, "윤대선": 19}#딕셔너리로 강의의 신청자 수 지정

                    menu2 = str(input("코드를 입력하세요")) #코드를 이용한 수강신청

                    print("교수님수업은 지금까지 %d명이 신청했습니다." % dict2[dict1[menu2]]) # 코드를 정장된 교수님이름으로 변경
                    if dict2[dict1[menu2]]>= 49: #강의 신청자수를 최대49명의로 제한
                        print("수강신청할 수 없습니다.")
                    else:
                        print("수강신청에 성공했습니다")
                        print("%s 교수님 수업을 신청했습니다." % dict1[menu2])
                elif time == 2:
                    dict3 = {"9032": "조극훈", "9033": "김문희", "9802": "김화경"}
                    dict4 = {"조극훈": 49, "김문희": 16, "김화경": 17}

                    menu3 = str(input("코드를 입력하세요"))

                    print("교수님수업은 지금까지 %d명이 신청했습니다." % dict4[dict3[menu3]])
                    if dict4[dict3[menu3]]>= 49:
                        print("수강신청할 수 없습니다.")
                    else:
                        print("수강신청에 성공했습니다")
                        print("%s 교수님 수업을 신청했습니다." % dict3[menu3])
                elif time == 3:
                    dict5 = {"9035": "최준호", "9036": "엄현섭", "9128": "윤대선"}
                    dict6 = {"조극훈": 49, "김문희": 16, "김화경": 17}

                    menu4 = str(input("코드를 입력하세요"))

                    print("교수님수업은 지금까지 %d명이 신청했습니다." % dict6[dict5[menu4]])
                    if dict6[dict5[menu4]]>= 49:
                        print("수강신청할 수 없습니다.")
                    else:
                        print("수강신청에 성공했습니다")
                        print("%s 교수님 수업을 신청했습니다." % dict5[menu4])
            else:
                print("없는 번호입니다")
                print("번호를 다시 입력해주세요")
                continue

        elif subject == 2:

            my = int(input("1.프로그래밍기초와실습  2.공학물리"))
            if my==1:
                pp=int(input("1.수123 2.수678"))
                if pp==1:
                    dict7 = {"1006": "박옥자"}
                    dict8 = {"박옥자": 48}

                    menu5 = str(input("코드를 입력하세요"))

                    print("교수님수업은 지금까지 %d명이 신청했습니다." % dict8[dict7[menu5]])
                    if dict8[dict7[menu5]] >= 49:
                        print("수강신청할 수 없습니다.")
                    else:
                        print("수강신청에 성공했습니다")
                        print("%s 교수님 수업을 신청했습니다." % dict7[menu5])
                if pp==2:
                    dict11 = {"1004": " 박옥자"}
                    dict12 = {"박옥자": 48}

                    menu10 = str(input("코드를 입력하세요"))

                    print("교수님수업은 지금까지 %d명이 신청했습니다." % dict12[dict11[menu10]])
                    if dict12[dict11[menu10]] >= 49:
                        print("수강신청할 수 없습니다.")
                    else:
                        print("수강신청에 성공했습니다")
                        print("%s 교수님 수업을 신청했습니다." % dict11[menu10])

            elif my==2:
                py=int(input("1.금123(a) 2.금123(b)"))
                if py==1:
                    dict9 = {"1234": "이규행","2345":"이영배"}
                    dict10 = {"이규행": 0,"이영배": 0}

                    menu6 = str(input("코드를 입력하세요"))

                    print("교수님수업은 지금까지 %d명이 신청했습니다." % dict10[dict9[menu6]])
                    if dict10[dict9[menu6]] >= 49:
                        print("수강신청할 수 없습니다.")
                    else:
                        print("수강신청에 성공했습니다")
                        print("%s 교수님 수업을 신청했습니다." % dict9[menu6])
        elif subject == 3:
            while (3):
                # 수강생 관리 프로그램
                print(" ==== 수강생 관리 프로그램 ====")
                print("1.수강생 정보")
                print("2.수강신청 목록 작성및 수정")
                print("3.종료")

                num = input("번호를 입력하세요")
                # 위에 등록했던 수강생 정보를 보기쉽게 정리
                if num == '1':
                    dict_ai = {"이름:": name, "나이:": age, "전공:": major, "학번:": class1}
                    for i, k in enumerate(dict_ai):
                        print(i, ":", k, dict_ai[k])



                elif num == '2':
                    # "위에 있던 강의 목록을 전부 딕셔너리로 저장"
                    dictA = {"0091": "조극훈(월123):사고와표현", "0092": "김문희(월123):사고와표현", "0093": "김화경(월123):사고와표현",
                             "0094": "최준호(월123):사고와표현",
                             "0095": "윤대선(월789):사고와표현", "9032": "조극훈(월789):사고와표현", "9033": "김문희(월789):사고와표현",
                             "9802": "김화경(월789):사고와표현",
                             "9035": "최준호(화678):사고와표현", "9036": "엄현섭(화678):사고와표현", "9128": "윤대선(화678):사고와표현",
                             "1006": "박옥자(수123):프로그램","1004":"박옥자(수678)프로그램",
                             "1234": "이규행(금123)공학물리", "2345": "이영배(금123)공학물리"}
                    listb = []  # 수강신청한 강의를 등록할 리스트 생성
                    n = int(input("등록할 과목의 개수를 적어주세요 "))
                    for x in range(n):  # 반복문을 통해 수강신청한 강의의 개수만큼 input문 반복
                        print("---------------------------------------")
                        abc = input("수강신청한 과목의 코드를 적어주세요")
                        print("---------------------------------------")
                        print("%s 교수님수업을 등록했습니다." % dictA[abc])

                        listb.append(dictA[abc])  # 생성된 리스트에 강의목록 추가
                    print(listb)  # 등록한 강의 보기
                    sp = input("수정하시겠습니까?y/n")  # 들록한 강의 정보 수정
                    if sp == 'y':
                        sp1 = int(input("1.삭제, 2.추가"))
                        if sp1 == 1:
                            avf = input("삭제할 코드를 입력하세요")
                            listb.remove(dictA[avf])  # remove 함수를 통해 들록한 강의 삭제
                            print(listb)
                        elif sp1 == 2:
                            abg = input("추가할 코드를 입력하세요")
                            listb.append(dictA[abg])  # append 함수를 통해 강의 추가
                            print(listb)
                        else:
                            print("번호를 다시 입력해주세요")
                            continue
                    else:
                        print("문자를 다시 입력해 주세요")
                        continue

                else:
                    print("프로그램을 마치겠습니다")
                    exit()
        else:
            exit()























































