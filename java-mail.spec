%include	/usr/lib/rpm/macros.java
Summary:	JavaMail - Java mail system
Summary(pl.UTF-8):	JavaMail - system pocztowy w Javie
Name:		javamail
Version:	1.4.1
Release:	1
License:	restricted, non-distributable (Sun Binary Code License - see LICENSE.txt)
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/products/javamail/downloads/
Source0:	%{name}-%(echo %{version} | tr . _).zip
# NoSource0-md5:	21296bdf2e55f2449ab4471b02503a5b
NoSource:	0
URL:		http://java.sun.com/products/javamail/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jaf
Requires:	jpackage-utils
Requires:	jre >= 1.1
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

%package doc
Summary:	JavaMail documentation
Summary(pl.UTF-8):	Dokumentacja do JavaMail
Group:		Development/Languages/Java

%description doc
JavaMail documentation.

%description doc -l pl.UTF-8
Dokumentacja do JavaMail.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
cp -a mail.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mail.jar

# put into our own dir so other implementations can override symlinks
cp -a lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
for a in lib/*.jar; do
	ln -s %{name}/${a##*/} $RPM_BUILD_ROOT%{_javadir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt COMPAT.txt LICENSE.txt NOTES.txt README.txt SSLNOTES.txt distributionREADME.txt
%{_javadir}/javamail-%{version}.jar
%{_javadir}/mail.jar
# lib symlinks
%{_javadir}/dsn.jar
%{_javadir}/imap.jar
%{_javadir}/mailapi.jar
%{_javadir}/pop3.jar
%{_javadir}/smtp.jar
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar

%files doc
%defattr(644,root,root,755)
%doc demo docs
