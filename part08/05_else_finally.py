def check(text):
    print(f"[{text}]")
    try:
        number = int(text)
    except ValueError:
        print("  except : 숫자가 아님")
    else:
        print("  else   : 변환 성공", number)
    finally:
        print("  finally: 언제나 실행")

check("42")
check("마흔둘")
