Name            : cpanel-php-dep
Summary         : Virtual package provides proper dependency resolution for php packages when using cpanel-php
Version         : 5.4.%{BUILD_NUMBER}
Release         : 2
BuildArch       : noarch
Provides        : php
Requires        : cpanel-php54
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.noarch.rpm

Group           : Servers/Basic Web Server
License         : None



%description



%install
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}-"*.noarch.rpm



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root (probably fine..)"
fi



%prep

%build

%files

%pre

%post

%changelog

