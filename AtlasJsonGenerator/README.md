## 功能
用于自动生成TwinStar.ToolKit的第18项功能**Atlas 解包**所需要的`.atlas.json`文件。



## 配置
`config.json`文件为配置文件，内容及作用如下：
```json5
{
    "checkFormat":false,
    //检查输入格式功能，开启后会检查输入的参数是否为.png或.PTX后缀
    //貌似没什么作用的功能，所以默认设置关闭，我也不知道当时为啥要写这段验证代码（
    //如果只打算使用下面第一中拖放文件运行的方式可以考虑开启这项功能
    //注意，要是开启了这项功能，下面第二点使用命令行方式中例子里最后那两种输入参数的格式就无法正常使用了
    //而如果你不开启他，反正就一个一次性程序，有问题让他程序崩掉也没关系，所以我代码里写这么多验证是干什么，果然还是没有用的功能（
    "resourcePath":""
    //RESOURCES.PTX文件解包出来的RESOURCES.json文件的路径，程序生成.atlas.json文件所必要的参考文件
    //建议使用RESOURCES.json文件的绝对路径，相对路径容易出问题，可以只填写到文件夹的路径像 D:/floder 这样
    //如果这项设置为空字符或者null的情况下，会在当前路径下寻找RESOURCES.json文件，如果是在terminal通过命令运行当前路径就是terminal所在路径，如果是拖动文件A到start.bat上打开则是文件A所在路径
}
```




## 使用方式
1. 将需要生成`.atlas.json`文件的atlas文件（`.png`和`.PTX`格式均可）拖到start.bat上运行即可
2. 或者可以直接在本目录下打开terminal，输入`python ./AtlasJsonGenerator [atlas的名称（带分辨率）]`,以需要生成`.atlas.json`的是`PLANTSUNFLOWER_1536_00`文件,以下几种形式的命令均可：
```cmd
python ./atlasJsonGenerator.py PLANTSUNFLOWER_1536_00.png
python ./atlasJsonGenerator.py PLANTSUNFLOWER_1536_00.PTX
python ./atlasJsonGenerator.py PLANTSUNFLOWER_1536_00
python ./atlasJsonGenerator.py PLANTSUNFLOWER_1536
```
