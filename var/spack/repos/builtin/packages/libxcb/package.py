##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Libxcb(Package):
    """The X protocol C-language Binding (XCB) is a replacement
    for Xlib featuring a small footprint, latency hiding, direct
    access to the protocol, improved threading support, and
    extensibility."""

    homepage = "http://xcb.freedesktop.org/"
    url      = "http://xcb.freedesktop.org/dist/libxcb-1.11.tar.gz"

    version('1.11', '1698dd837d7e6e94d029dbe8b3a82deb')
    version('1.11.1', '118623c15a96b08622603a71d8789bf3')

    depends_on("python", type='build')
    depends_on("xcb-proto")
    depends_on("pkg-config", type='build')
    depends_on("libpthread-stubs")
    depends_on('libxau')

    def patch(self):
        filter_file(
            'typedef struct xcb_auth_info_t {',
            'typedef struct {',
            'src/xcb.h')

    def install(self, spec, prefix):
        env['PKG_CONFIG_PATH'] = env[
            'PKG_CONFIG_PATH'] + ':/usr/lib64/pkgconfig'
        configure("--prefix=%s" % prefix)

        make()
        make("install")
