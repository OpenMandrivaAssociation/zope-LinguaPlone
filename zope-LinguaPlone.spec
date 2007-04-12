%define product		LinguaPlone
%define ver		0.8.5
%define rel		2

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python


Summary:	LinguaPlone aims to be *the* multilingual/translation solution for Plone
Name:		zope-%{product}
Version:	%{ver}
Release:	%mkrel %{rel}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/linguaplone/releases/%{version}/LinguaPlone-%{version}.tar.bz2
URL:		http://plone.org/products/linguaplone
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	plone >= 2.1
Requires:	zope-Archetypes
Requires:	zope-PloneLanguageTool

%description
 LinguaPlone aims to be *the* multilingual/translation solution for
Plone, and achieves this by being as transparent as possible and by
minimizing the impact for existing applications and Plone itself.

 It utilizes Archetypes references to do the translation, and all content
is left intact both on install and uninstall - thus, it will not disrupt
your content structure in any way. It also works with WebDAV and FTP.

 LinguaPlone doesn't require a particular hierarchy of content, and will
work with any layout of your content space.

Some benefits of LinguaPlone

  - Totally transparent, install-and-go.

  - Each translation is a discrete object, and can be workflowed individually.

  - This also means that it works with WebDAV and FTP.

  - Translations are kept track of using AT references.

  - You can multilingual-enable your types without affecting their operation
outside LinguaPlone.

  - Even if you uninstall LinguaPlone after adding multilingual content, all
your content will be intact and will work as separate objects! The only thing
that will be inactive is the references between the objects. If you re-install
it, they will be back. It's very non-intrusive.

  - Supporting multilingual capabilities is a 4 (!) line addition to your
Archetypes class, and does not alter the functionality of the class when used
outside LinguaPlone.

  - Fully integrated with ATContentTypes, so the basic content types are
translatable.

  - Supports language-independent fields (example: dates, first/last names) for
fields you wiant to be the same across translations, and updated in all 
languages if one of them changes.

  - Uses the notion of Canonical versions, so you can do interesting things 
with workflow, like invalidate all translations of a document when the master 
copy has changed.


%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-, root, root, 0755)
%{software_home}/Products/*



