Name            : cpanel-php-dep
Summary         : Virtual package provides proper dependency resolution for php packages when using cpanel-php
Version         : 1.0.%{BUILD_NUMBER}
Release         : 2
BuildArch       : noarch
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.noarch.rpm

Group           : Servers/Basic Web Server
License         : None
Packager        : PoiXson <support@poixson.com>
URL             : http://yum.poixson.com/



### Packages ###
%package -n cpanel-php54-dep
Summary         : Virtual package provides proper dependency resolution for php packages when using cpanel-php54
Requires        : cpanel-php54
Provides        : php

%package -n cpanel-php55-dep
Summary         : Virtual package provides proper dependency resolution for php packages when using cpanel-php55
Requires        : cpanel-php55
Provides        : php

%package -n cpanel-php56-dep
Summary         : Virtual package provides proper dependency resolution for php packages when using cpanel-php56
Requires        : cpanel-php54
Provides        : php



%description
%description -n cpanel-php54-dep
%description -n cpanel-php55-dep
%description -n cpanel-php56-dep



%install
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}-"*.noarch.rpm



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root (probably fine..)"
fi



%files -n cpanel-php54-dep
%files -n cpanel-php55-dep
%files -n cpanel-php56-dep

