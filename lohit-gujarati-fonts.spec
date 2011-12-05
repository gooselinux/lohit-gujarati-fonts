%global fontname lohit-gujarati
%global fontconf 66-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.4.4
Release:        3%{?dist}
Summary:        Free Gujarati font

Group:          User Interface/X
License:        GPLv2 with exceptions
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Patch1: bug-549319-578031.patch
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Gujarati truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
%patch1 -p1 -b .1-fix-font-conf

%build
make

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README ChangeLog.old


%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- Resolves: bug 586856

* Mon Dec 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- fixed bug 548686, license field
- Resolves: bug 550987

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4.4-1.1
- Rebuilt for RHEL 6

* Wed Oct 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release wuth bugfix 529637
- update in upstream url

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs
	
* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
