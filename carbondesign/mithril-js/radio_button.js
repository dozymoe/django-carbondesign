import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class Radio extends FormNode
{
    NODE_PROPS = ['exclude', 'vertical', 'left']
    TEMPLATES = ['items', ...FormNode.TEMPLATES]

    prepare(vnode, values, context)
    {
        if (vnode.attrs.vertical)
        {
            values.wrapper_class.push('bx--radio-button-group--vertical');
        }
        if (vnode.attrs.left)
        {
            values['class'].push('bx--radio-button-wrapper--label-left');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('fieldset.bx--fieldset', null,
  [
    m('legend',
      {
        'class': `bx--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    m('div.bx--form-item', null,
      m('div',
        {
          'class': `bx--radio-button-group ${values.wrapper_class}`,
        },
        this.tmpl('items', vnode, values, context))),
  ])
//##
        );
    }

    render_tmpl_items(vnode, values, context)
    {
        let value = this.bound_field.value();
        let excludes = vnode.attrs.exclude || [];

        let items = [], ii = 0;
        for (let [group, val, txt] of this.choices(context))
        {
            let props = {};
            if (val === value)
            {
                props['checked'] = '';
            }
            if (excludes.indexOf(val) != -1)
            {
                props['disabled'] = '';
            }
            items.push(
//##
m('div',
  {
    'class': `bx--radio-button-wrapper ${values['class']}`,
  },
  [
    m('input.bx--radio-button',
      {
        id: values.id,
        type: 'radio',
        value: val,
        name: this.bound_field.name,
        tabindex: 0,
        ...values.props,
      },
    m('label.bx--radio-button__label',
      {
        'for': values.id,
      },
      [
        m('span.bx--radio-button__appearance'),
        m('span.bx--radio-button__label-text', null, txt),
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
