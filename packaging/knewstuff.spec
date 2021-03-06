# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       knewstuff

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 module for downloading application assets
Version:    5.3.0
Release:    2
Group:      System/Base
License:    LGPL2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  knewstuff.yaml
Source101:  knewstuff-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  karchive-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel

%description
KDE Frameworks 5 Tier 3 module for downloading application assets


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   karchive-devel
Requires:   kcompletion-devel
Requires:   kconfig-devel
Requires:   kcoreaddons-devel
Requires:   ki18n-devel
Requires:   kiconthemes-devel
Requires:   kio-devel
Requires:   kitemviews-devel
Requires:   ktextwidgets-devel
Requires:   kwidgetsaddons-devel
Requires:   kxmlgui-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%find_lang knewstuff5_qt --with-qt --all-name || :

%files -f knewstuff5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5NewStuff.so.*
%{_kf5_datadir}/knewstuff/
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/knewstuff_version.h
%{_kf5_includedir}/KNewStuff3
%{_kf5_libdir}/libKF5NewStuff.so
%{_kf5_cmakedir}/KF5NewStuff
%{_kf5_mkspecsdir}/*.pri
# >> files devel
# << files devel
