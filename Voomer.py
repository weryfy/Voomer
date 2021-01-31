logo = '''
\\\\            //   ||$$$$|   ||$$   \\\\   //   ||===| \\\\   //
 \\\\          //    ||        ||  $   \\\\ //    ||      \\\\ //
  \\\\        //     ||$$$$|   ||$$     \\|/     ||==|    \\|/
   \\\\  ||  //      ||        || \\\\     &      ||        &
    \\\\//\\\\//       ||$$$$|   ||  \\\\    $      ||        $
'''

print("%s\n\r\n\r" % logo)
print("██████████████  https://github.com/weryfy  ██████████████")
print("\n\r\n\r\n\r")

import os,sys,math
try:
	import shodan
except Exception as e:
	print ('install shodan module with command :\nWindows : pip install shodan\nLinux   : sudo apt-get install python3-pip&& pip3 install shodan')
	sys.exit(-1)

SHODAN_API_KEY = input("Enter Shodan API Key > ")
if(SHODAN_API_KEY == ""):
	SHODAN_API_KEY = "PSKINdQe1GyxGgecYz2191H2JoS9qvgD"
print("SHODAN API KEY => %s" % SHODAN_API_KEY)

try:
    api = shodan.Shodan(SHODAN_API_KEY)
    #SearchQuery
    SearchQuery = input("Enter Query> ")
    print("Found results: %s\n\n" % api.search(SearchQuery)['total'])
    #SearchQuery
    filename = input("Enter filename for save: ")
    handle = open(filename, "w")
    for ed in range(math.ceil(api.search(SearchQuery)['total']/100)):
        for service in api.search(SearchQuery,page=ed)['matches']:
            handle.write('%s:%s\n' % (service['ip_str'], service['port']))
    handle.close()
except Exception as e:
    print ('Error: %s' % e)
    sys.exit(1)





