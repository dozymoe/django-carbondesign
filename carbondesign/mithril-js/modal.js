import m from 'mithril/hyperscript';
//-
import { Node } from './base';
import { Button } from './button';


export class Modal extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['label', 'heading', 'footer']

    prepare(vnode, values, context)
    {
        values.txt_close = gettext("close modal");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-modal': '',
    id: values.id,
    'class': 'bx--modal ' + values['class'],
    role: 'dialog',
    'aria-modal': true,
    'aria-labelledby': values.id + '-label',
    'aria-describedby': values.id + '-heading',
    tabindex: -1,
    ...values.props,
  },
  [
    m('div.bx--modal-container', null,
      [
        m('div.bx--modal-header', null,
          [
            this.slot('label', vnode, values, context),
            this.slot('heading', vnode, values, context),
            m('button.bx--modal-close',
              {
                type: 'button',
                'data-modal-close': '',
                'aria-label': values.txt_close,
              },
              m('svg.bx--modal-close__icon',
                {
                  focusable: false,
                  preserveAspectRatio: 'xMidYMid meet',
                  style: {'will-change': 'transform'},
                  xmlns: 'http://www.w3.org/2000/svg',
                  width: 16,
                  height: 16,
                  viewBox: '0 0 16 16',
                  'aria-hidden': true,
                },
                m('path',
                  {
                    d: "M12 4.7L11.3 4 8 7.3 4.7 4 4 4.7 7.3 8 4 11.3 4.7 12 \
                        8 8.7 11.3 12 12 11.3 8.7 8z",
                  })
                )
              ),
          ]),
        m('div.bx--modal-content',
          {
            tabindex: 0,
          },
          values.child),
        m('div.bx--modal-content--overflow-indicator'),
        this.slot('footer', vnode, values, context),
      ]),
    m('span', {tabindex: 0}),
  ])
//##
        );
    }

    render_slot_label(vnode, values, context)
    {
        return (
//##
m('p',
  {
    'class': 'bx--modal-header__label bx--type-delta ' + values['class'],
    id: values.id + '-label',
    ...values.props
  },
  values.child)
//##
        );
    }

    render_slot_heading(vnode, values, context)
    {
        return (
//##
m('p',
  {
    'class': 'bx--modal-header__heading bx--type-beta ' + values['class'],
    id: values.id + '-heading',
    ...values.props
  },
  values.child)
//##
        );
    }

    render_slot_footer(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': 'bx--modal-footer ' + values['class'],
    ...values.props
  },
  values.child)
//##
        );
    }
}


export class ModalTrigger extends Button
{
    NODE_PROPS = ['target', ...Button.NODE_PROPS]

    prepare(vnode, values, context)
    {
        super.prepare(vnode, values, context);

        values.props.push(['data-modal-target', '#' + vnode.attrs.target]);
    }

    after_prepare(vnode, values, context)
    {
        super.after_prepare(vnoce, values, context);

        if (!values['child'])
        {
            values['child'] = gettext("Show modal");
        }
    }
}
