import ProductSwitcher from 'carbon-components/src/components/ui-shell/product-switcher';
import m from 'mithril/hyperscript';
import m_tostring from 'mithril-node-render';
//-
import { FormNode, Node, clean_attr_value, modify_svg } from './base';

export class UiActionSwitcher extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['svg_open', 'svg_close']
    NODE_PROPS = ['target']
    REQUIRED_PROPS = ['label', 'target']
    DEFAULT_TAG = 'button'

    prepare(vnode, values, context)
    {
        values.txt_close_menu = gettext("Close menu");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--header__menu-trigger bx--header__action ${values['class']}`,
    'aria-label': values.label,
    title: values.label,
    'data-navigation-menu-panel-label-expand': values.label,
    'data-navigation-menu-panel-label-collapse': values.txt_close_menu,
    'data-panel-switcher-target': `#${vnode.attrs.target}`,
    ...values.props,
  },
  [
    this.slot('svg_close', ...arguments),
    this.slot('svg_open', ...arguments),
  ])
//##
        );
    }

    oncreate(vnode)
    {
        this.attached = ProductSwitcher.init(vnode.dom,
                {
                    attribInitTarget: 'data-panel-switcher-target',
                });
    }

    onremove(vnode)
    {
        this.attached.release();
    }

    render_slot_svg_close(vnode, values, context)
    {
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                fill: 'currentColor',
                style: {
                    width: '20px',
                    height: '20px',
                },
                'aria-hidden': true,
                'class': 'bx--navigation-menu-panel-expand-icon',
            })
    }

    render_slot_svg_open(vnode, values, context)
    {
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                fill: 'currentColor',
                style: {
                    width: '20px',
                    height: '20px',
                },
                'aria-hidden': true,
                'class': 'bx--navigation-menu-panel-collapse-icon',
            })
    }
}


export class UiSwitcher extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['id']
    DEFAULT_TAG = 'aside'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': 'bx--panel--overlay',
    id: values.id,
    'data-panel-switcher': true,
  },
  m('div.bx--panel-switcher', values.child))
//##
        );
    }
}


export class UiSwitcherSearch extends FormNode
{
    NODE_PROPS = ['placeholder']

    prepare(vnode, values, context)
    {
        values.txt_clear = gettext("Clear search input");
    }

    prepare_element_props(vnode, props, context)
    {
        props['class'].append('bx--search-input');
        props.placeholder = vnode.attrs.placeholder || gettext("Search");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--panel-switcher__search',
  m('div.bx--form-item',
    m('div.bx--search.bx--search--sm.bx--search--shell',
      {
        'data-search': '',
        role: 'search',
      },
      [
        this.tmpl('label', ...arguments),
        this.tmpl('element', ...arguments),
        m('svg.bx--search-magnifier',
          {
            width: 16,
            height: 16,
            viewBox: '0 0 16 16',
          },
          m('path',
            {
              d: 'M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11zm4.936-1.\
                  27l4.563 4.557-.707.708-4.563-4.558a6.5 6.5 0 1 1 .707\
                  -.707z',
              'fill-rule': 'nonzero',
            })),
        m('button.bx--search-close.bx--search-close--hidden',
          {
            title: value.txt_clear,
            'aria-label': values.txt_clear,
          },
          m('svg',
            {
              width: 16,
              height: 16,
              viewBox: '0 0 16 16',
              xmlns: 'http://www.w3.org/2000/svg',
            },
            m('path',
              {
                d: 'M8 6.586L5.879 4.464 4.464 5.88 6.586 8l-2.122 2.121 \
                   1.415 1.415L8 9.414l2.121 2.122 1.415-1.415L9.414 8l2.\
                   122-2.121-1.415-1.415L8 6.586zM8 16A8 8 0 1 1 8 0a8 8 0 \
                   0 1 0 16z',
                'fill-rule': 'evenodd',
              }))),
      ])))
//##
        );
    }
}


export class UiSwitcherHeader extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'p'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--panel-switcher__subheader ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class UiSwitcherItem extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return m('div.bx--panel-switcher__item', values.child);
    }
}


export class UiSwitcherMenu extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'ul'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--panel-switcher__panel-list ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class UiSwitcherMenuSection extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']
    NODE_PROPS = ['menu_label']
    CLASS_AND_PROPS = ['overflow']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.menu_label)
        {
            values.overflow_props.push(['aria-label', vnode.attrs.menu_label]);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('li.bx--panel-list__item',
  [
    m('a.bx--panel-link',
      {
        tabindex: 0,
        href: 'javascript:void(0)',
      },
      this.slot('icon', ...arguments),
      m('span.bx--panel-link__name', values.label)),
    m('div',
      {
        'data-overflow-menu': '',
        tabindex: 0,
        'class': `bx--overflow-menu ${values.overflow_class}`,
        ...values.overflow_props,
      },
      [
        m('svg',
          {
            width: 3,
            height: 15,
            viewBox: '0 0 3 15',
          },
          m('path',
           {
             d: 'M0 1.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 1 1-3 0M0 7.5a1.5 1.5 0 \
                 1 1 3 0 1.5 1.5 0 1 1-3 0M0 13.5a1.5 1.5 0 1 1 3 0 1.5 1.5 \
                 0 1 1-3 0',
           })),
        m('ul.bx--overflow-menu-options.bx--overflow-menu--flip',
          {
            tabindex: -1,
            'data-floating-menu-direction': 'bottom',
          },
          values.child)
      ]),
  ])
//##
        );
    }

    render_slot_icon(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--panel-switcher__icon ${values['class']}`,
  },
  modify_svg(values.child,
    {
      focusable: 'false',
      preserveAspectRatio: 'xMidYMid meet',
      fill: 'currentColor',
      style: {
        width: '20px',
        height: '20px',
      },
      'aria-hidden': true,
    }))
//##
        );
    }
}


export class UiSwitcherMenuItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['active']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.active)
        {
            values.props.push(['data-floating-menu-primary-focus', '']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('li.bx--overflow-menu-options__option.bx--overflow__item',
  m('button',
    {
      'class': `bx--overflow-menu-options__btn ${values['class']}`,
      title: clean_attr_value(m_tostring(values.child)),
    }))
//##
        );
    }
}
