import sys

#comment

print(sys.argv)

if '-h' in sys.argv or '--help' in sys.argv:
    print("\t\tИнформация выводится если при запуске файла\n\t\tпрописать модификатор -h или --help")
    print("\n\t\tЧтобы начать писать с новой строки вызовите\n\t\tследующий принт или используйте \\n для перевода\n\t\tкоретки на новую строку")
    print("\n\t\tВ помощь сайт http://cppstudio.com/post/256/,\n\t\tпервая ссылка в гугле с основными символами")
