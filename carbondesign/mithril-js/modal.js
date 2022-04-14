import ModalComponent from 'carbon-components/src/components/modal/modal';
import m from 'mithril/hyperscript';
//-
import { Node } from './base';
import { Button } from './button';

export class Modal extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['label', 'heading', 'footer']
    NODE_PROPS = ['id', 'variant', 'has_form', 'size', 'can_scroll']
    CLASS_AND_PROPS = ['container', 'content', 'close']
    POSSIBLE_VARIANT = ['danger']

    prepare(vnode, values, context)
    {
        values.txt_close = gettext("close modal");

        let variant = vnode.attrs.variant;
        if (variant)
        {
            values['class'].push(`bx--modal--${variant}`);
        }

        if (this.slots.label)
        {
            values.props.push(['aria-labelledby', `label-${values.id}`]);
        }
        if (this.slots.heading)
        {
            values.props.push(['aria-describedby', `heading-${values.id}`]);
        }

        if (vnode.attrs.has_form)
        {
            values.content_class.push('bx--modal-content--with-form');
        }

        let size = vnode.attrs.size;
        if (size)
        {
            values.container_class.push(`bx--modal-container--${size}`);
        }

        if (!vnode.attrs.has_form && !this.slots.footer)
        {
            values.close_props.push(['data-modal-primary-focus', true]);
        }

        if (vnode.attrs.can_scroll)
        {
            values.content_props.push(['tabindex', '0']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-modal': true,
    id: values.id,
    'class': `bx--modal ${values['class']}`,
    role: 'dialog',
    'aria-modal': 'true',
    tabindex: -1,
    ...values.props,
  },
  [
    m('div.bx--modal-container',
      {
        'class': values.container_class,
        ...values.container_props,
      },
      [
        m('div.bx--modal-header', null,
          [
            this.slot('label', ...arguments),
            this.slot('heading', ...arguments),
            m('button',
              {
                'class': `bx--modal-close ${values.close_class}`,
                type: 'button',
                'data-modal-close': true,
                'aria-label': values.txt_close,
                ...values.close_props,
              },
              m('svg.bx--modal-close__icon',
                {
                  focusable: false,
                  preserveAspectRatio: 'xMidYMid meet',
                  fill: 'currentColor',
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
        m('div',
          {
            'class': `bx--modal-content ${values.content_class}`,
            ...values.content_props,
          },
          values.child),
        m('div.bx--modal-content--overflow-indicator'),
        this.slot('footer', ...arguments),
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
    'class': `bx--modal-header__label bx--type-delta ${values['class']}`,
    id: `label-${values.id}`,
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
    'class': `bx--modal-header__heading bx--type-beta ${values['class']}`,
    id: `heading-${values.id}`,
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
    'class': `bx--modal-footer ${values['class']}`,
    ...values.props
  },
  values.child)
//##
        );
    }
}


export class ModalTrigger extends Button
{
    NODE_PROPS = ['target', ...(new Button).NODE_PROPS]

    prepare(vnode, values, context)
    {
        super.prepare(...arguments);
        values.props.push(['data-modal-target', `#${vnode.attrs.target}`]);
    }

    after_prepare(vnode, values, context)
    {
        super.after_prepare(...arguments);
        if (!values.child)
        {
            values.child = gettext("Show modal");
        }
    }

    oncreate(vnode)
    {
        this.attached = ModalComponent.init(vnode.dom);
    }

    onremove(vnode)
    {
        this.attached.release();
    }
}
