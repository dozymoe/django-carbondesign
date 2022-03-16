import m from 'mithril/hyperscript';
//-
import { FormNode, Node } from './base';

export class StructuredList extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['header']

    render_default(vnode, values, context)
    {
        return (
//##
m('section.bx--structured-list', null,
  [
    m('div.bx--structured-list-thead', null,
      m('div.bx--structured-list-row.bx--structured-list-row--header-row', null,
        this.slot('header', vnode, values, context))),
    m('div.bx--structured-list-tbody', null, values.child),
  ])
//##
        );
    }
}


export class StructuredListSelect extends FormNode
{
    WANT_CHILDREN = true
    SLOTS = ['header']

    prepare(vnode, values, context)
    {
        context.bound_field = this.bound_field;
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('section.bx--structured-list.bx--structured-list--selection',
  {
    'data-structured-list': '',
  },
  [
    m('div.bx--structured-list-thead', null,
      m('div.bx--structured-list-row.bx--structured-list-row--header-row', null,
        this.slot('header', vnode, values, context))),
    m('div.bx--structured-list-tbody', null, values.child),
  ])
//##
        );
    }
}


export class StructuredListTh extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--structured-list-th ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class StructuredListTd extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['nowrap']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.nowrap)
        {
            values['class'].push('bx--structured-list-content--nowrap');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--structured-list-td ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class StructuredListTr extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['value']

    prepare(vnode, values, context)
    {
        this.bound_field = context.bound_field;
        if (this.bound_field)
        {
            let selected_values = this.bound_field.value();
            if (selected_values.indexOf(vnode.attrs.value) != -1)
            {
                values.label_class.push('bx--structured-list-row--selected');
                values.props.push(['checked', '']);
            }
        }
    }

    render_default(vnode, values, context)
    {
        if (this.bound_field)
        {
            return (
//##
m('label',
  {
    'aria-label': values.label,
    'class': `bx--structured-list-row ${values.label_class}`,
    tabindex: 0,
    ...values.label_props,
  },
  [
    values.child,
    m('input',
      {
        tabindex: -1,
        'class': `bx--structured-list-input ${values['class']}`,
        value: vnode.attrs.value,
        type: 'radio',
        name: this.bound_field.name,
        title: values.label,
        ...values.props,
      }),
    m('div.bx--structured-list-td', null,
      m('svg.bx--structured-list-svg',
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
        [
          m('path',
            {
              d: 'M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,\
                  1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z',
            }),
          m('path',
            {
              d: 'M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z',
              'data-icon-path': 'inner-path',
              opacity: 0,
            }),
        ])),
  ])
//##
            );
        }

        return (
//##
m('div.bx--structured-list-row', null, values.child)
//##
        );
    }
}
