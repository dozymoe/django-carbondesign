import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';


export class CheckBox extends FormNode
{
    MODES = ['default', 'inside']
    NODE_PROPS = ['mixed']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.disabled)
        {
            values.props.push(['disabled', 'disabled']);
        }

        if (vnode.attrs.mixed && this.mode === 'inside')
        {
            values.label_props.push(['data-contained-checkbox-state', 'mixed']);
        }
    }

    prepare_element_attributes(vnode, attrs, default_attrs, context)
    {
        attrs['class'].push('bx--checkbox');

        if (vnode.attrs.mixed)
        {
            attrs['aria-checked'] = 'mixed';
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item.bx--checkbox-wrapper', null,
  [
    values.element,
    m('label',
      {
        'for': values.id,
        'class': 'bx--checkbox-label ' + values.label_class,
        ...values.label_props,
      },
      values.label),
  ])
//##
        );
    }

    render_inside(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item.bx--checkbox-wrapper', null,
  [
    m('label',
      {
        'for': values.id,
        'class': 'bx--checkbox-label ' + values.label_class,
        ...values.label_props,
      },
      [
        values.element,
        values.label,
      ]),
  ])
//##
        );
    }
}
