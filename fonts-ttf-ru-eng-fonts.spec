%define pkgname 122658-ru-eng-fonts

Summary: Russian Fonts
Name: fonts-ttf-ru-eng-fonts
Version: 1.0
Release: 2
License: GPL
Group: System/Fonts/True type
URL: https://opendesktop.org/content/show.php/ru-eng-fonts?content=122658
Source0: %{pkgname}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools

%description
There are 8 fonts in this package,which include english and russian alphabet.

%prep
%setup -q -n ru-eng-fonts

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/ru-eng

install -m 644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/ru-eng
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/ru-eng > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/ru-eng/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/ru-eng/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/ru-eng \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-ru-eng:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi


%files
%defattr(-,root,root,-)
#%doc License.txt 
#COPYING
%dir %{_datadir}/fonts/TTF/ru-eng
%{_datadir}/fonts/TTF/ru-eng/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/ru-eng/fonts.dir
%{_datadir}/fonts/TTF/ru-eng/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-ru-eng:pri=50



%changelog
* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 1.0-1mdv2012.0
+ Revision: 691022
- fix spec
- imported package fonts-ttf-ru-eng-fonts

