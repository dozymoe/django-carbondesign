import m from 'mithril/hyperscript';
//-
import { FormNode, Node, modify_svg } from './base';

export class Toolbar extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--toolbar ${values['class']}`,
    'data-toolbar': '',
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class ToolbarSearch extends Node
{
    prepare(vnode, values, context)
    {
        values.txt_toolbar_search = gettext("Toolbar Search");
        values.txt_clear_search = gettext("Clear search input");
        if (!values.label)
        {
            values.label = gettext("Search");
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--search.bx--search--sm.bx--toolbar-search',
  {
    role: 'search',
    'data-search': '',
    'data-toolbar-search': '',
  },
  [
    m('label',
      {
        'for': `search__input-${values.id}`,
        'class': `bx--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    m('input.bx--search-input',
      {
        type: 'text',
        'for': `search__input-${values.id}`,
        placeholder: values.label,
      }),
    m('button.bx--toolbar-search__btn',
      {
        'aria-label': values.txt_toolbar_search,
      },
      m('svg.bx--search-magnifier',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          width: 16,
          height: 16,
          viewBox: '0 0 16 16',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,\
                8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5   C2,4,4,2,\
                6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z',
          }))),
    m('button.bx--search-close.bx--search-close--hidden',
      {
        title: values.txt_clear,
        'aria-label': values.txt_clear,
      },
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          width: 16,
          height: 16,
          viewBox: '0 0 32 32',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 \
                17.4 22.6 24 24 22.6 17.4 16 24 9.4z',
          }))),
  ])
//##
        );
    }
}


export class ToolbarItem extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']

    prepare(vnode, values, context)
    {
        values.txt_list = gettext("List of options");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--overflow-menu',
  {
    'data-overflow-menu': '',
    tabindex: 0,
    'aria-label': values.txt_list,
  },
  [
    this.slot('icon', vnode, values, context),
    m('ul.bx--overflow-menu-options', null, values.child),
  ])
//##
        );
    }

    render_slot_icon(vnode, values, context)
    {
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                fill: 'currentColor',
                'class': 'bx--overflow-menu__icon bx--toolbar-filter-icon',
                style: {
                    width: 16,
                    height: 16,
                },
                'aria-hidden': true,
            })
    }
}


export class ToolbarMultiSelect extends FormNode
{
    render_default(vnode, values, context)
    {
        let selected = this.bound_field.value();

        let items = [];
        let ii = 0;
        for (let [group, val, txt] of this.choices(context))
        {
            let id = `${values.id}-${ii}`, props = {};
            if (!ii)
            {
                props['data-floating-menu-primary-focus'] = '';
            }
            if (selected.indexOf(val) != -1)
            {
                props['checked'] = '';
            }
            items.push(
//##
m('li.bx--toolbar-menu__option', null,
  [
    m('input.bx--checkbox',
      {
        id: id,
        type: 'checkbox',
        value: val,
        name: this.bound_field.name,
        ...props,
      }),
    m('label.bx--checkbox-label', {'for': id}, txt),
  ])
//##
            );
            ii++;
        }

        if (items.length)
        {
            return m.fragment(null, items);
        }
    }
}


export class ToolbarRadioButton extends FormNode
{
    render_default(vnode, values, context)
    {
        return (
//##
m('fieldset.bx--radio-button-group',
  {
    'data-row-height': '',
  },
  [
    m('legend.bx--visually-hidden', null, values.label),
    this.tmpl('items', vnode, values, context),
  ])
//##
        );
    }

    render_tmpl_items(vnode, values, context)
    {
        let selected = this.bound_field.value();

        let items = [], ii = 0;
        for (let [group, val, txt] of this.choices(context))
        {
            let id = `${values.id}-${ii}`, props = {};
            if (!ii)
            {
                props['data-floating-menu-primary-focus'] = '';
            }
            if (val === selected)
            {
                props['checked'] = '';
            }
            items.push(
//##
m('li.bx--toolbar-menu__option', null,
  [
    m('input.bx--radio-button',
      {
        id: id,
        type: 'radio',
        value: val,
        name: this.bound_field.name,
        ...props,
      }),
    m('label.bx--radio-button__label',
      {
        'for': id,
      },
      [
        m('span.bx--radio-button__appearance'),
        txt,
      ]),
  ])
//##
            );
            ii++;
        }

        if (items.length)
        {
            return m.fragment(null, items);
        }
    }
}


export class ToolbarHeading extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('li',
  {
    'class': `bx--toolbar-menu__title ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class ToolbarDivider extends Node
{
    render_default(vnode, values, context)
    {
        return m('hr.bx--toolbar-menu__divider')
    }
}
