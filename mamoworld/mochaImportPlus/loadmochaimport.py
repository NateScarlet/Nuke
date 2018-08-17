import imp
import os
import sys
import nuke

# adds the correct plugin path for this version of NUKE


def load():
    supportedMagicNumbers = ['03f30d0a', 'd1f20d0a']

    try:
        magicNumberOfThisVersion = imp.get_magic().encode('hex')
        if magicNumberOfThisVersion in supportedMagicNumbers:
            pathToThisVersion = "./version_" + magicNumberOfThisVersion
            nuke.pluginAddPath(pathToThisVersion)
        else:
            raise Exception("MochaImport+ for NUKE: unsupported version of Python:" +
                            sys.version + "(magic number:" + magicNumberOfThisVersion + ")")

    except Exception as e:
        import traceback
        nuke.tprint(traceback.format_exc())  # Just in case
        msg = 'ERROR: %s' % e
        if nuke.GUI:
            nuke.message(msg)
        else:
            nuke.tprint(msg)
