#include<iostream>
#include<list>
#include<vector>
#include<map>
#include<string>
#include<cstdlib>
using namespace std;

map<string, double> digit;
map<string, string> text;

string shell(string show = ">>>")
{
    char temp[100];
    cout<<show;
    cin.getline(temp, 100);
    string command(temp);
    return command;
}

list<string> parse(string text)
{
    list<string> code;
    string temp = " ";
    char the;
    bool dotext = false;

    for(int i = 0; i < text.size(); i++)
    {
        the = text.at(i);
        if(the == '\"' && dotext == false)
        {
            dotext = true;
            temp = "\"";
        }
        else if(the == '\"' && dotext == true)
        {
            code.push_back(temp);
            dotext = false;
        }
        else if(dotext == true) temp += the;
        else if(the == ' ')
        {
            code.push_back(temp);
        }
        else
        {
            if(temp != " ") temp += the;
            else temp = the;
        }
    }
    return code;
}

void savedigit(string name, double var)
{
    digit[name] = var;
}

string gettext(string name)
{
    return text[name];
}

double getdigit(string name)
{
    return digit[name];
}

void savetext(string name, string var)
{
    text[name] = var;
}

void print(string var)
{
    if(var.at(0) == '\"')
    {
        for(int i = 1; i < var.size(); i++) cout<<var.at(i);
        cout<<endl;
    }
    else cout<<gettext(var)<<endl;
}

int run(list<string> code)
{
    string name, dothen = " ", the;
    bool dovar = false;

    for(int i = 0; i < code.size(); i++)
    {
        the = code.front();
        if(dothen != " ")
        {
            if(dothen == "print") print(the);
            else if(dothen == "digit")
            {
                if(dovar = false)
                {
                    name = the;
                    dovar = true;
                }
                else savedigit(name, atof(the.c_str()));
            }
            else if(dothen == "text")
            {
                if(dovar = false)
                {
                    name = the;
                    dovar = true;
                }
                else savetext(name, the);
            }
        }
        else dothen = the;
    }
}

int main()
{
    string code;
    while(true)
    {
        code = shell();
        if(code == "quit") break;
        else run(parse(code));
    }
    return 0;
}