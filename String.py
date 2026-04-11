print("pengenalan string")

#1.  Menggunakan qoute ''  ""
"dengan menggunakan single quote '...'"
'dengan menggunakan double quote "..."'

#2. menggunakan tanda \
print('hari jum\'at')
print('isn\'t it')

#atau bisa saja quote O/C diganti ""

#3. Tab (longkap)
print("several\toracles")
print("several\t\t\toracles")

#4. Backslash \
    #jika alhabet string sama dengan command
print("c:\\several\noracles")
print("c:\\several\\noracles")

#5. Backspace / Menghapus Jarak  \b  
print("several \boracles")

#6. Newline (LF(linefeed)) paragraf baru \n
    #LINUX / UNIX / MACOS
print("several, \noracles") 

#7. Newline (CR(Carriage Return)) / menghapus paragraf sebelum \r
    #PC LAMA
print("several\r, oracles")

#8. Newline (CRLF(linefeed Carriage Return)) / menghapus paragraf sebelum \r
    #WINDOWS
print("several\r\n, oracles")

#9. Raw String r"...."
    #apapun yang ada dibelakang r, makan akan dianggap string
print(r"several\r\n, oracles")

#10. Multiline Literal String (""""
#                              ....   
#                              """")
print(""""
several
oracles
""")

#11. Multiline Literal String Raw
print(r""""
www.several\
oracles.id
""")
