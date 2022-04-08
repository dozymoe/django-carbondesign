import HeaderNav from 'carbon-components/src/components/ui-shell/header-nav';
import HeaderSubmenu from 'carbon-components/src/components/ui-shell/header-submenu';
import NavigationMenu from 'carbon-components/src/components/ui-shell/navigation-menu';
import SideNav from 'carbon-components/src/components/ui-shell/side-nav';

export default function()
{
    let el;
    el = document.querySelector('button.bx--header__menu-trigger');
    if (el) NavigationMenu.init(el);

    HeaderNav.init();
    HeaderSubmenu.init();
    SideNav.init();
}
