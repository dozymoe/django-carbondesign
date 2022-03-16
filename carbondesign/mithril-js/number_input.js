import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class NumberInput extends FormNode
{
    MODES = ['default', 'mobile']
    NODE_PROPS = ['nolabel', 'light']

    prepare(vnode, values, context)
    {
        values.txt_increase = gettext("increase number input");
        values.txt_decrease = gettext("decrease number input");

        if (vnode.attrs.nolabel)
        {
            values['class'].push('bx--number--nolabel');
        }
        if (vnode.attrs.light)
        {
            values['class'].push('bx--number--light');
        }
        if (this.bound_field.help_text)
        {
            values['class'].push('bx--number--helpertext');
        }
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        if (this.bound_field.errors)
        {
            props.role = 'alert';
            props['aria-atomic'] = 'true';
        }
    }

    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-invalid': '',
      'data-numberinput': '',
      'class': `bx--number ${values['class']}`,
    },
    [
      this.tmpl('label', vnode, values, context),
      m('div.bx--number__input-wrapper', null,
        [
          values.element,
          this.tmpl('icon_invalid', vnode, values, context),
          m('div.bx--number__controls', null,
            [
              this.tmpl('btn_incr', vnode, values, context),
              this.tmpl('btn_decr', vnode, values, context),
            ]),
        ]),
      m('div.bx--form-requirement', null, values.form_errors),
      this.tmpl('help', vnode, values, context),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-numberinput': '',
      'class': `bx--number ${values['class']}`,
    },
    [
      this.tmpl('label', vnode, values, context),
      m('div.bx--number__input-wrapper', null,
        [
          values.element,
          m('div.bx--number__controls', null,
            [
              this.tmpl('btn_incr', vnode, values, context),
              this.tmpl('btn_decr', vnode, values, context),
            ]),
        ]),
      this.tmpl('help', vnode, values, context),
    ]))
//##
        );
    }

    render_mobile(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-invalid': '',
      'data-numberinput': '',
      'class': `bx--number bx--number--mobile ${values['class']}`,
    },
    [
      this.tmpl('label', vnode, values, context),
      m('div.bx--number__input-wrapper', null,
        [
          this.tmpl('btn_decr', vnode, values, context),
          values.element,
          this.tmpl('btn_decr', vnode, values, context),
        ]),
      m('div.bx--form-requirement', null, values.form_errors),
      this.tmpl('help', vnode, values, context),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-numberinput': '',
      'class': `bx--number bx--number--mobile ${values['class']}`,
    },
    [
      this.tmpl('label', vnode, values, context),
      m('div.bx--number__input-wrapper', null,
        [
          this.tmpl('btn_decr', vnode, values, context),
          values.element,
          this.tmpl('btn_decr', vnode, values, context),
        ]),
      this.tmpl('help', vnode, values, context),
    ]))
//##
        );
    }

    render_tmpl_label(vnode, values, context)
    {
        if (!vnode.attrs.nolabel)
        {
            return (
//##
m('label',
  {
    'for': values.id,
    'class': `bx--label ${values.label_class}`,
    ...values.label_props,
  },
  values.label)
//##
            );
        }
    }

    render_tmpl_icon_invalid(vnode, values, context)
    {
        return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': 'bx--number__invalid',
    width: 16,
    height: 16,
    viewBox: '0 0 16 16',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        d: 'M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,\
            4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.\
            3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z',
      }),
    m('path',
      {
        d: 'M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.\
            8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z',
        'data-icon-path': 'inner-path',
        opacity: 0,
      }),
  ])
//##
        );
    }

    render_tmpl_btn_incr(vnode, values, context)
    {
        return (
//##
m('button',
  {
    'aria-label': values.txt_increase,
    'class': 'bx--number__control-btn up-icon',
    type: 'button',
    'aria-live': 'polite',
    'aria-atomic': true,
  },
  m('svg',
    {
      focusable: false,
      preserveAspectRatio: 'xMidYMid meet',
      xmlns: 'http://www.w3.org/2000/svg',
      fill: 'currentColor',
      width: 8,
      height: 4,
      viewBox: '0 0 8 4',
      'aria-hidden': true,
    },
    m('path', {d: 'M0 4L4 0 8 4z'})))
//##
        );
    }

    render_tmpl_btn_decr(vnode, values, context)
    {
        return (
//##
m('button',
  {
    'aria-label': values.txt_decrease,
    'class': 'bx--number__control-btn down-icon',
    type: 'button',
    'aria-live': 'polite',
    'aria-atomic': true,
  },
  m('svg',
    {
      focusable: false,
      preserveAspectRatio: 'xMidYMid meet',
      xmlns: 'http://www.w3.org/2000/svg',
      fill: 'currentColor',
      width: 8,
      height: 4,
      viewBox: '0 0 8 4',
      'aria-hidden': true,
    },
    m('path', {d: 'M8 0L4 4 0 0z'})))
//##
        );
    }
}
