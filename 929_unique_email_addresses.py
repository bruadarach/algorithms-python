'''
Every email consists of a local name and a domain name, separated by the @ sign.
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
Besides lowercase letters, these emails may contain '.'s or '+'s.
If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)
If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
'''


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        result = []

        for email in emails:
            email = email.split('@')

            front = email[0]
            end = email[1]

            if '+' in front:
                idx = front.find('+')
                front = front[0:idx]
            front = front.replace('.', '')
            result.append(front+'@'+end)

        return len(set(result))

# (runtime / memory)
#  44 ms / 14.6 MB



'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        result = set()
        
        for email in emails:  
            front,end = email.split('@')
            front = front.split('+')[0].replace('.','')
            result.add(front+'@'+end)
                   
        return len(result)
'''
# (runtime / memory)
#  60 ms / 14.5 MB



'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        result = []

        for email in emails:
            front, end = email.split('@')
            
            if '+' in front:
                front = front.split('+')[0]
            front = front.replace('.', '')
            front = front+'@'+end
            
            if front not in result:
                result.append(front)

        return len(result)
'''
# (runtime / memory)
#  60 ms / 14.6 MB

