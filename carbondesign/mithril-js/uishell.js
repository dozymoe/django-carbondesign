import m from 'mithril/hyperscript';
import DOMPurify from 'dompurify';
//-
import { Node, modify_svg } from './base';

export class UiShell extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['title', 'title_prefix', 'navigation', 'links', 'actions',
            'sidenav', 'switcher']
    NODE_PROPS = ['href', 'label_prefix']
    DEFAULT_TAG = 'header'

    prepare(vnode, values, context)
    {
        values.txt_skip_menu = gettext("Skip to main content");
        values.txt_open_menu = gettext("Open menu");
        values.txt_close_menu = gettext("Close menu");

        values.long_label = this.label(context);
    }

    render_default(vnode, values, context)
    {
        return (
//##
m.fragment(null,
  [
    m(values.tag,
      {
        'class': `bx--header ${values['class']}`,
        role: 'banner',
        'aria-label': values.long_label,
        'data-header': '',
        ...values.props,
      },
      [
        m('a.bx--skip-to-content',
          {
            href: '#main-content',
            tabindex: 0,
          },
          values.txt_skip_menu),
        this.tmpl('hamburger', vnode, values, context),
        m('a.bx--header__name',
          {
            href: vnode.attrs.href,
          },
          this.tmpl('title', vnode, values, context)),
        this.slot('links', vnode, values, context),
        this.slot('actions', vnode, values, context),
      ]),
    this.slot('sidenav', vnode, values, context),
    this.slot('switcher', vnode, values, context),
    this.slot('navigation', vnode, values, context),
    m('.bx--content', null, values.child),
  ])
//##
        );
    }

    render_slot_navigation(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--navigation ${values['class']}`,
    id: `navigation-menu-${values.id}`,
    hidden: '',
    'data-navigation-menu': '',
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_slot_links(vnode, values, context)
    {
        return (
//##
m('nav',
  {
    'class': `bx--header__nav ${values['class']}`,
    'aria-label': values.label,
    'data-header-nav': '',
  },
  m('ul.bx--header__menu-bar',
    {
      'aria-label': values.label,
      ...values.props,
    },
    values.child))
//##
        );
    }

    render_slot_actions(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--header__global ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_slot_title_prefix(vnode, values, context)
    {
        return (
//##
m('span',
  {
    'class': `bx--header__name--prefix ${values['class']}`,
    ...values.props,
  },
  [
    values.child,
    m.trust('&nbsp;'),
  ])
//##
        );
    }

    render_tmpl_title(vnode, values, context)
    {
        if (this.slots.title_prefix)
        {
            return (
//##
m.fragment(null,
  [
    this.slot('title_prefix', vnode, values, context),
    this.slot.title ? this.slot('title', vnode, values, context) : values.label,
  ])
//##
            );
        }
        if (this.slot.title)
        {
            return this.slot('title', vnode, values, context);
        }
        return values.label;
    }

    render_tmpl_hamburger(vnode, values, context)
    {
        if (this.slots.navigation)
        {
            return (
//##
m('button.bx--header__menu-trigger.bx--header__action',
  {
    'aria-label': values.txt_open_menu,
    title: values.txt_open_menu,
    'data-navigation-menu-panel-label-expand': values.txt_open_menu,
    'data-navigation-menu-panel-label-collapse': values.txt_close_menu,
    'data-navigation-menu-target': `#navigation-menu-${values.id}`,
  },
  [
    m('svg',
      {
        focusable: false,
        preserveAspectRatio: 'xMidYMid meet',
        style: {'will-change': 'transform'},
        xmlns: 'http://www.w3.org/2000/svg',
        'aria-hidden': true,
        'class': 'bx--navigation-menu-panel-collapse-icon',
        width: 20,
        height: 20,
        viewBox: '0 0 32 32',
      },
      m('path',
        {
          d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4\
              22.6 24 24 22.6 17.4 16 24 9.4z',
        })),
    m('svg',
      {
        focusable: false,
        preserveAspectRatio: 'xMidYMid meet',
        style: {'will-change': 'transform'},
        xmlns: 'http://www.w3.org/2000/svg',
        'aria-hidden': true,
        'class': 'bx--navigation-menu-panel-expand-icon',
        width: 20,
        height: 20,
        viewBox: '0 0 20 20',
      },
      m('path',
        {
          d: 'M2 14.8H18V16H2zM2 11.2H18V12.399999999999999H2zM2 \
              7.6H18V8.799999999999999H2zM2 4H18V5.2H2z',
        })),
  ])
//##
            );
        }
    }
}


export class UiLink extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['submenu']

    prepare(vnode, values, context)
    {
        this.is_submenu = context.navlink_submenu;
        if (this.is_submenu)
        {
            values.props.tabindex = -1;
        }
        else
        {
            values.props.tabindex = 0;
        }
        if (this.slots.submenu)
        {
            context.navlink_submenu = true;
        }
    }

    render_default(vnode, values, context)
    {
        let cleaned_child = DOMPurify.sanitize(values.child);

        if (this.slots.submenu)
        {
            return (
//##
m('li.bx--header__submenu',
  {
    'data-header-submenu': '',
  },
  [
    m('a',
      {
        'class': `bx--header__menu-item bx--header__menu-title ${values['class']}`,
        'aria-haspopup': true,
        'aria-expanded': false,
        ...values.props,
      },
      [
        values.child,
        m('svg.bx--header__menu-arrow',
          {
            width: 12,
            height: 7,
            'aria-hidden': true,
          },
          m('path',
            {
              d: 'M6.002 5.55L11.27 0l.726.685L6.003 7 0 .685.726 0z',
            })),
      ]),
    m('ul.bx--header__menu',
      {
        'aria-label': cleaned_child,
        ...values.slot_submenu_props,
      },
      this.slot('submenu', vnode, values, context)),
  ])
//##
            );
        }
        if (this.is_submenu)
        {
            return (
//##
m('li',
  {
    role: 'none',
  },
  m('a',
    {
      'class': `bx--header__menu-item ${values['class']}`,
      ...values.props,
    },
    m('span.bx--text-truncate--end', null, values.child)))
//##
            );
        }
        return (
//##
m('li', null,
  m('a',
    {
      'class': `bx--header__menu-item ${values['class']}`,
      ...values.props,
    },
    values.child))
//##
        );
    }
}


export class UiNavSection extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--navigation-section ${values['class']}`,
    ...values.props,
  },
  m('ul.bx--navigation-items', null, values.child))
//##
        );
    }
}


export class UiNavItem extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['submenu', 'icon']
    NODE_PROPS = ['active', 'icon_size']

    prepare(vnode, values, context)
    {
        if (context.navitem_submenu)
        {
            values['class'].push('bx--navigation__category-item');
            if (vnode.attrs.active)
            {
                values['class'].push('bx--navigation__category-item--active');
            }
        }
        else
        {
            values['class'].push('bx--navigation-item');
            if (vnode.attrs.active)
            {
                values['class'].push('bx--navigation-item--active');
            }
        }

        if (this.slots.submenu)
        {
            context.navitem_submenu = true;
        }
        if (this.slots.icon)
        {
            values['class'].push('bx--navigation-item--icon');
        }
    }

    render_default(vnode, values, context)
    {
        if (this.slots.submenu)
        {
            return (
//##
m('li',
  {
    'class': values['class'],
    ...values.props,
  },
  m('div.bx--navigation__category', null,
    [
      m('button.bx--navigation__category-toggle',
        {
          type: 'button',
          'aria-haspopup': true,
          'aria-expanded': false,
          'aria-controls': `category-${values.id}-menu`,
        },
        [
          this.slot('icon', vnode, values, context),
          m('div.bx--navigation__category-title', null,
            [
              values.child,
              m('svg',
                {
                  'aria-hidden': true,
                  width: 20,
                  height: 20,
                  xmlns: 'http://www.w3.org/2000/svg',
                  viewBox: '0 0 32 32',
                },
                m('path',
                  {
                    d: 'M16 22L6 12l1.414-1.414L16 19.172l8.586-8.586L26 12 \
                        16 22z',
                  })),
            ]),
        ]),
      this.slot('submenu', vnode, values, context),
    ]))
  values.child)
//##
            );
        }
        return (
//##
m('li',
  {
    'class': values['class'],
  },
  m('a.bx--navigation-link', values.props,
    [
      this.slot('icon', vnode, values, context),
      values.child,
    ]))
//##
        );
    }

    render_slot_submenu(vnode, values, context)
    {
        return (
//##
m('ul',
  {
    'class': `bx--navigation__category-items ${values['class']}`,
    id: `category-${values.id}-menu`,
  },
  values.child)
//##
        );
    }

    render_slot_icon(vnode, values, context)
    {
        let size = vnode.attrs.icon_size || 20;
        return (
//##
m('div',
  {
    'class': `bx--navigation-icon ${values['class']}`,
  },
  modify_svg(values.child,
    {
      focusable: 'false',
      preserveAspectRatio: 'xMidYMid meet',
      style: {
        'will-change': 'transform',
        width: `${size}px`,
        height: `${size}px`,
      },
      'aria-hidden': true,
    }))
//##
        );
    }
}


export class UiSideNav extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['header', 'footer', 'title_icon', 'title', 'switcher']
    NODE_PROPS = ['fixed']
    DEFAULT_TAG = 'aside'

    prepare(vnode, values, context)
    {
        values.txt_label = gettext("Side navigation");
        values.txt_close = gettext("Close the side navigation menu");
        values.txt_close_help = gettext("Toggle the expansion state of the navigation");
        values.txt_switcher = gettext("Switcher");

        if (vnode.attrs.fixed)
        {
            values['class'].push('bx--side-nav--fixed');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--side-nav ${values['class']}`,
    'data-side-nav': '',
    ...values.props,
  },
  m('nav.bx--side-nav__navigation',
    {
      role: 'navigation',
      'aria-label': values.txt_label,
    },
    [
      this.slot('header', vnode, values, context),
      m('ul.bx--side-nav__items', null, values.child),
      this.slot('footer', vnode, values, context),
    ]))
//##
        );
    }

    render_slot_header(vnode, values, context)
    {
        return (
//##
m('header',
  {
    'class': `bx--side-nav__header ${values['class']}`,
    ...values.props,
  },
  [
    this.slot('title_icon', vnode, values, context),
    m('div.bx--side-nav__details', null,
      [
        this.slot('title', vnode, values, context),
        this.slot('switcher', vnode, values, context),
      ]),
  ])
//##
        );
    }

    render_slot_header(vnode, values, context)
    {
        if (this.slots.title_icon || this.slots.title || this.slots.switcher)
        {
            return (
//##
m('footer',
  {
    'class': `bx--side-nav__footer ${values['class']}`,
    ...values.props,
  },
  m('button.bx--side-nav__toggle',
    {
      type: 'button',
      title: values.txt_close,
    },
    [
      m('div.bx--side-nav__icon', null,
        [
          m('svg.bx--side-nav__icon--collapse.bx--side-nav-collapse-icon',
            {
              focusable: false,
              preserveAspectRatio: 'xMidYMid meet',
              style: {'will-change': 'transform'},
              xmlns: 'http://www.w3.org/2000/svg',
              'aria-hidden': true,
              width: 20,
              height: 20,
              viewBox: '0 0 32 32',
            },
            m('path',
              {
                d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 \
                    16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z',
              })),
          m('svg.bx--side-nav__icon--expand.bx--side-nav-expand-icon',
            {
              focusable: false,
              preserveAspectRatio: 'xMidYMid meet',
              style: {'will-change': 'transform'},
              xmlns: 'http://www.w3.org/2000/svg',
              'aria-hidden': true,
              width: 20,
              height: 20,
              viewBox: '0 0 32 32',
            },
            m('path',
              {
                d: 'M22 16L12 26 10.6 24.6 19.2 16 10.6 7.4 12 6z',
              })),
        ]),
      m('span.bx--assistive-text', null, values.txt_close_help),
    ]))
//##
            );
        }
    }

    render_slot_title_icon(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--side-nav__icon ${values['class']}`,
  },
  modify_svg(values.child,
    {
      preserveAspectRatio: 'xMidYMid meet',
      style: {
        'will-change': 'transform',
        width: '20px',
        height: '20px',
      },
      'aria-hidden': true,
    }))
//##
        );
    }

    render_slot_title(vnode, values, context)
    {
        let cleaned_child = DOMPurify.sanitize(values.child);

        return (
//##
m('h2',
  {
    'class': `bx--side-nav__title ${values['class']}`,
    title: cleaned_child,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_slot_switcher(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--side-nav__switcher ${class}`,
  },
  [
    m('label.bx--assistive-text',
      {
        'for': `side-nav-switcher-${values.id}`,
      },
      values.txt_switcher),
    m('select.bx--side-nav__select',
      {
        id: `side-nav-switcher-${values.id}`,
        ...values.props,
      },
      values.child),
    m('div.bx--side-nav__switcher-chevron', null,
      m('svg',
        {
          'aria-hidden': true,
          width: 20,
          height: 20,
          xmlns: 'http://www.w3.org/2000/svg',
          viewBox: '0 0 32 32',
        },
        m('path',
          {
            d: 'M16 22L6 12l1.414-1.414L16 19.172l8.586-8.586L26 12 16 22z',
          }))),
  ])
//##
        );
    }
}


export class UiSideNavOption extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('option',
  {
    'class': `bx--side-nav__option ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class UiSideNavItem extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['submenu', 'icon']
    NODE_PROPS = ['active', 'icon_size']

    prepare(vnode, values, context)
    {
        if (context.navitem.submenu)
        {
            values['class'].push('bx--side-nav__menu-item');
            if (vnode.attrs.active)
            {
                values['class'].push('bx--side-nav__menu-item--active');
            }
        }
        else
        {
            values['class'].push('bx--side-nav__item');
            if (vnode.attrs.active)
            {
                values['class'].push('bx--side-nav__item--active');
            }
        }

        if (vnode.attrs.active)
        {
            values.link_class = 'bx--side-nav__link--current';
            values.props.push(['aria-current', 'page']);
        }
        else
        {
            values.link_class = '';
        }

        if (this.slots.submenu)
        {
            context.navitem_submenu = true;
        }
    }

    render_default(vnode, values, context)
    {
        if (this.slots.submenu)
        {
            return (
//##
m('li',
  {
    'class': values['class'],
  },
  [
    m('button.bx--side-nav__submenu',
      {
        type: 'button',
        'aria-haspopup': true,
        'aria-expanded': true,
        'aria-controls': `sidenav-${values.id}-menu`,
      },
      [
        this.slot('icon', vnode, values, context),
        m('span.bx--side-nav__submenu-title', null, values.child),
        m('div.bx--side-nav__icon.bx--side-nav__icon--small.bx--side-nav__submenu-chevron',
          null,
          m('svg',
            {
              'aria-hidden': true,
              width: 20,
              height: 20,
              xmlns: 'http://www.w3.org/2000/svg',
              viewBox: '0 0 32 32',
            },
            m('path',
              {
                d: 'M16 22L6 12l1.414-1.414L16 19.172l8.586-8.586L26 12 16 22z',
              }))),
      ]),
    m('ul.bx--side-nav__menu',
      {
        id: `sidenav-${values.id}-menu`,
        ...values.props,
      },
      this.slot('submenu', vnode, values, context)),
  ])
//##
            );
        }
        return (
//##
m('li'
  {
    'class': values['class'],
  },
  m('a',
    {
      'class': `bx--side-nav__link ${values.link_class}`,
      ...values.props,
    },
    [
      this.slot('icon', vnode, values, context),
      m('span.bx--side-nav__link-text', null, values.child),
    ]))
//##
        );
    }

    render_slot_icon(vnode, values, context)
    {
        let size = vnode.attrs.icon_size || 20;

        return (
//##
m('div',
  {
    'class': `bx--side-nav__icon bx--side-nav__icon--small ${values['class']}`,
  },
  values.child)
//##
        );
    }
}
