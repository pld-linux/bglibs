Summary:	Bruce Guenter's Libraries Collection
Summary(pl):	Zestaw bibliotek Bruce'a Guentera
Name:		bglibs
Version:	1.017
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://untroubled.org/bglibs/%{name}-%{version}.tar.gz
# Source0-md5:	27409cbd25480cbb3a9555766f3beb26
URL:		http://untroubled.org/bglibs/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# it cannot be installed in /usr/{include,lib} because of filename collisions
%define		_prefix		/usr/lib/bglibs

%description
Bruce Guenter's Libraries Collection.

%description -l pl
Zestaw bibliotek Bruce'a Guentera.

%prep
%setup -q

%build
echo '%{__cc} %{rpmcflags} -Wall' > conf-cc
echo '%{_prefix}' > conf-home
echo '%{__cc} %{rpmldflags}' > conf-ld

%{__make}

rm -f conf_home.c insthier.o installer
echo "$RPM_BUILD_ROOT%{_prefix}" > conf-home
%{__make} installer

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

./installer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%dir %{_prefix}
%{_prefix}/include
%{_prefix}/lib
