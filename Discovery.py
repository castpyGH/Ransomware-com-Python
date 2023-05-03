import os

#Função responsável por descobrir os arquivos do sistema.
def discoverFile(initial_path):
    extenions = [
    '3gp', '7z', 'aac', 'abw', 'ac3', 'ai', 'aif', 'aifc', 'aiff',
    'alac', 'ape', 'apk', 'appx', 'appxbundle', 'arc', 'arj', 'asc',
    'asf', 'asm', 'asp', 'aspx', 'atom', 'au', 'avi', 'awk', 'azw',
    'azw3', 'bat', 'bib', 'bin', 'bmp', 'bzip2', 'c', 'cpp', 'cs',
    'css', 'csv', 'cue', 'deb', 'dll', 'dmg', 'doc', 'docx', 'dot',
    'dotx', 'eot', 'epub', 'exe', 'f4a', 'f4b', 'f4p', 'f4v', 'flac',
    'flv', 'gif', 'gz', 'h', 'h264', 'htm', 'html', 'ico', 'ics',
    'jar', 'java', 'jpeg', 'jpg', 'js', 'json', 'jsp', 'key', 'ktx',
    'latex', 'log', 'lzh', 'm4a', 'm4b', 'm4p', 'm4v', 'mkv', 'mobi',
    'mov', 'mp3', 'mp4', 'mpeg', 'mpg', 'odp', 'ods', 'odt', 'oga',
    'ogg', 'ogv', 'otf', 'pdb', 'pdf', 'php', 'png', 'pot', 'potx',
    'pps', 'ppsx', 'ppt', 'pptx', 'ps', 'py', 'qt', 'rar', 'rpm',
    'rtf', 'rtx', 'rvb', 'scss', 'sh', 'sit', 'sitx', 'sqlite', 'svg',
    'swf', 'tar', 'tarbz2', 'targz', 'tex', 'tgz', 'ttf', 'txt', 'vob',
    'wav', 'webm', 'wma', 'wmv', 'woff', 'wpd', 'wps', 'xhtml', 'xml',
    'xpi', 'xsd', 'xsl', 'xslt', 'yaml', 'zip', '3g2', 'a', 'ai', 'apk', 
    'appimage', 'arw', 'as', 'as3', 'axa', 'bin',
    'blend', 'bz2', 'cgm', 'class', 'com', 'cr2', 'cr3', 'crw', 'csh', 'cue',
    'dat', 'deb', 'dif', 'dcm', 'dds', 'dng', 'dpx', 'drv', 'dtd', 'dwg',
    'dxf', 'efx', 'eps', 'erf', 'exe', 'fff', 'fits', 'fnt', 'fon', 'g3',
    'gbr', 'gho', 'gifv', 'gsm', 'gz', 'hdr', 'hqx', 'htc', 'htm', 'html',
    'icns', 'ico', 'indd', 'iso', 'jfif', 'jng', 'jp2', 'jpe', 'jpf', 'jpgm',
    'jpx', 'jtf', 'kar', 'kml', 'kmz', 'lnk', 'lwo', 'lz', 'lzma', 'lzx',
    'm', 'm2ts', 'm4v', 'mac', 'mcd', 'mdb', 'mdi', 'mef', 'mid', 'mim',
    'mix', 'mmf', 'mng', 'mos', 'mov', 'mp2', 'mpc', 'mpg', 'mpga', 'msp',
    'mx', 'nc', 'nef', 'nrg', 'nsf', 'obj', 'odb', 'odc', 'odf', 'odg',
    'ofr', 'oga', 'ogx', 'one', 'orf', 'otg', 'out', 'ov2', 'p12', 'p7b',
    'p7c', 'pab', 'pages', 'pct', 'pcx', 'pdb', 'pef', 'pict', 'pkpass',
    'pl', 'ply', 'ppam', 'pps', 'ppsm', 'ppsx', 'pptm', 'prc', 'psb',
    'psd', 'ptx', 'puz', 'qcp', 'qtvr', 'ra', 'raf', 'ram', 'raw', 'rm',
    'rpm', 'rss', 's3m', 'sar', 'sav', 'sdv', 'sf2', 'sfd', 'sis', 'sit',
    'skp', 'sldm', 'sldx', 'smc', 'srt', 'stl', 'sub', 'sv4cpio', 'svgz',
    'swc', 'swf', 'sys', 'tarz', 'texi', 'thmx', 'tif', 'tiff', 'tr', 'ttc',
    'ttx', 'twd', 'udf', 'utf8', 'vcard', 'vcf', 'vmdk', 'vob', 'vsd', 'wav',
    'wax', 'wbmp', 'wbxml', 'webp', 'wiz', 'wk1', 'wm', 'wma', 'wmv', 'wp5',
    'wpd', 'wps',  '3dm', '3ds', '3g2', '3gp', '7z', 'aac', 'aax', 'abw', 'ac3', 'accdb',
    'accdc', 'accde', 'accdp', 'accdr', 'accdt', 'accdu', 'acr', 'afm', 'ai',
    'aif', 'aifc', 'aiff', 'air', 'amfm', 'ani', 'apk', 'appimage', 'application',
    'arc', 'arw', 'as', 'as3', 'asc', 'ascx', 'asd', 'asf', 'ashx', 'asmx',
    'asp', 'aspx', 'asr', 'asx', 'atom', 'au', 'avi', 'axa', 'bak', 'bat',
    'bay', 'bmp', 'bz2', 'c', 'cab', 'caf', 'calx', 'cat', 'cbl', 'cc',
    'ccxml', 'cda', 'cdf', 'cdr', 'cdt', 'cdx', 'cer', 'cfg', 'cfm', 'cgi',
    'cgm', 'chm', 'class', 'clp', 'cmd', 'cmid', 'cod', 'coffee', 'com', 'config',
    'contact', 'core', 'cpio', 'cpp', 'cpt', 'cr2', 'cr3', 'crl', 'crt', 'crw',
    'cs', 'csh', 'csproj', 'css', 'csv', 'ctl', 'cue', 'cur', 'cxx', 'dcm',
    'dcr', 'dcs', 'ddd', 'deb', 'def', 'der', 'desktop', 'device', 'dib', 'dif',
    'dmg', 'dmp', 'dng', 'doc', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'dp',
    'dpg', 'dpx', 'drv', 'dtd', 'dwg', 'dxf', 'dxr', 'ebd', 'ebook', 'ecelp4800',
    'ecelp7470', 'ecelp9600', 'ecma', 'edm', 'edx', 'efx', 'eip', 'elf', 'emf',
    'eml', 'emp', 'emz', 'eot', 'eps', 'epub', 'erf', 'es', 'es3', 'esf',
    'etf', 'etx', 'exe', 'exr', 'ez', 'ez2', 'ez3', 'f4v', 'f77', 'f90',
    'fb2', 'fdf', 'fev', 'fig', 'fits', 'fla', 'flac', 'flv', 'fnt', 'fon',
    'fpx', 'frm', 'fsh', 'fsproj', 'fvi', 'g3', 'gac', 'gam', 'gb', 'gba',
    'gbc', 'gbr', 'gc', 'ged', 'gem', 'gho', 'gif', 'gifv', 'gml', 'gpx',
    'graffle', 'group', 'gs', 'gsm', 'gtar', 'gz', 'h', 'h261', 'h263', 'h264',
    'hdr']

    #Percorrendo os diretórios e arquivos na página inicial configurada em "initial_path"
    for dirpath, dirs, files in os.walk(initial_path):
        #Percorrendo cada item dentros dos ⬆️ arquivos "files" 
        for _file in files:
            #Criando o caminho absoludo do arquivo em cada sistema.
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            #Pegando a extensão de cada item
            ext = absolute_path.split(".")[-1]
            #Verificando se essa é uma das extenções alvo
            if ext in extenions:
                yield absolute_path

if __name__ == "__main__":
    x = discoverFile(os.getcwd())
    for i in x:
        print(i)