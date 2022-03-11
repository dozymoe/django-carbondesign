import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class Slider extends FormNode
{
    NODE_PROPS = ['min', 'max', 'step', 'light']

    prepare(vnode, values, context)
    {
        values.txt_slider = gettext("slider");
        values.min = vnode.attrs.min || 0;
        values.max = vnode.attrs.max || 100;
        values.step = vnode.attrs.step || 1;
        values.value = this.bound_field.value();

        if (vnode.attrs.light)
        {
            values['class'].push('bx--slider-text-input--light');
        }

        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.wrapper_class.push('bx--slider--disabled');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item', null,
  [
    m('label',
      {
        'class': `bx--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    m('div.bx--slider-container', null,
      [
        m('label.bx--slider__range-label',
          {
            id: `slider-input-box_bottom-range-label-${values.id}`,
          },
          values.min),
        m('div',
          {
            'class': `bx--slider ${values.wrapper_class}`,
            'data-slider': '',
            'data-slider-input-box': `#${values.id}`,
          },
          [
            m('div.bx--slider__thumb', {tabindex: 0}),
            m('div.bx--slider__track'),
            m('div.bx--slider__filled-track'),
            m('input.bx--slider__input',
              {
                'aria-label': values.txt_slider,
                id: `slider-${values.id}`,
                type: 'range',
                step: values.step,
                min: values.min,
                max: values.max,
                value: values.value,
          ]),
        m('label.bx--slider__range-label',
          {
            id: `slider-input-box_top-range-label-${values.id}`,
          },
          values.max),
        m('input',
          {
            id: values.id,
            'aria-labelledby': `slider-input-box_bottom-range-label-${values.id} slider-input-box_top-range-label-${values.id}`,
            type: 'number',
            'class': `bx--text-input bx--slider-text-input ${values['class']}`,
            placeholder: values.min,
            value: values.value,
          }),
      ]),
  ])
//##
        );
    }
}
