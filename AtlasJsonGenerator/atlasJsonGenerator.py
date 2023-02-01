import json
import sys
import platform
import os

def run():
    programPath=os.path.split(os.path.realpath(__file__))[0]
    with open(programPath+"/config.json",'r') as f:
        config=json.load(f)
    # the file's full path
    path = sys.argv[1]
    print(path)##
    if platform.system() == "Windows":
        path = path.replace('\\', '/')
    sections = path.split('/')
    length = len(sections)
    # get file's name
    if length > 1:
        fileName = sections[length-1]
    else:
        fileName = sections[0]
    sections = fileName.split('.')
    length=len(sections)
    # is it png||ptx format?
    if (config["checkFormat"]):
        length = len(sections)
        strErrorInput = "格式不正确，输入文件路径应为.png或.ptx格式"
        if length < 2:
            print(strErrorInput)
            return
        suffix = sections[-1].lower()
        if suffix != "png" or suffix != "ptx":
            print(strErrorInput)
            return
    # get atlas' id
    if length > 1:
        sections.pop()
    print(sections)###
    outputName = '.'.join(sections)
    sections=outputName.split('_')
    if sections[-1]=="00":
        sections.pop()
    id='_'.join(sections)
    # query relevant information in resources file
    resourceFileName="RESOURCES.json"
    resourcePath=resourceFileName
    if config["resourcePath"]!=None:
        if config["resourcePath"].strip()!='':
            resourcePath=config["resourcePath"]
            if platform.system() == "Windows":
                resourcePath=resourcePath.replace('\\', '/')
            sections=resourcePath.split('/')
            if sections[-1]!=resourceFileName:
                sections.append(resourceFileName)
                resourcePath='/'.join(sections)
    with open(resourcePath, 'r') as f:
        resource = json.load(f,strict=False)
    groups = resource["groups"]
    flag = False
    print(id)###
    for o in groups:
        if o["id"].lower() == id.lower():
            ls = o["resources"]
            flag = True
            break
    if (flag == False):
        print("没找到相关信息，请检查输入是否正确")
        return
    # generate the atlas json
    '''
    characterName=input("请输入pam文件名:").lower()
    sections=characterName.split('.')
    characterName=sections[0]
    '''
    atlasJson = {"size": [ls[0]["width"], ls[0]["height"]]}
    sprite = {}
    for o in ls[1:]:
        '''
        sections=o["id"].split('_')
        if len(sections[-1])==1:
            tail='_'+sections[-2]+'_'+sections[-1]
        else:
            tail='_'+sections[-1]
        id=characterName+tail
        '''
        id=o["path"][-1]
        sprite.update({id: {"position": [o["ax"], o["ay"]], "size": [o["aw"], o["ah"]]}})
    atlasJson.update({"sprite": sprite})
    with open(outputName+".atlas.json",'w') as f:
        json.dump(atlasJson,f)

if __name__ == "__main__":
    run()
