# TODO:
# - not tested after changing Source0 !!!
# - what about docs, examples etc. ?
# - build from sources. It is possible now.
%include	/usr/lib/rpm/macros.java
Summary:	JavaMail - Java mail system
Summary(pl.UTF-8):	JavaMail - system pocztowy w Javie
Name:		javamail
Version:	1.4.1
Release:	1.1
License:	CDDL
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/products/javamail/downloads/
Source0:	https://maven-repository.dev.java.net/nonav/repository/javax.mail/jars/mail-1.4.1.jar
# Source0-md5:	584010e5e62f4fa4b8ccfdf35a2c3a8a
URL:		http://java.sun.com/products/javamail/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jaf
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The JavaMail(TM) API provides a set of abstract classes that model a
mail system. The API provides a platform independent and protocol
independent framework to build Java technology-based mail and
messaging applications.

%description -l pl.UTF-8
API JavaMail(TM) daje zestaw klas abstrakcyjnych tworzących system
pocztowy. API daje niezależne od platformy i protokołu środowisko do
tworzenia aplikacji pocztowych i komunikacyjnych w oparciu o Javę.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a $SOURCE0 $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mail.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/javamail-%{version}.jar
%{_javadir}/mail.jar
