import ProductSwitcher from 'carbon-components/src/components/ui-shell/product-switcher';
import m from 'mithril/hyperscript';
//-
import { Node, modify_svg } from './base';

export class UiShellAction extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['svg_open', 'svg_close']
    NODE_PROPS = ['target']
    DEFAULT_TAG = 'button'

    oncreate(vnode)
    {
        this.attached = ProductSwitcher.init(vnode.dom);
    }

    onremove(vnode)
    {
        this.attached.release();
    }

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
    'data-product-switcher-target': `#${vnode.attrs.target}`,
    ...values.props,
  },
  [
    this.slot('svg_open', ...arguments),
    this.slot('svg_close', ...arguments),
    values.child,
  ])
//##
        );
    }

    render_slot_svg_close(values, context)
    {
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                style: {
                    'will-change': 'transform',
                    width: 20,
                    height: 20,
                },
                'aria-hidden': true,
                'class': 'bx--navigation-menu-panel-collapse-icon',
            })
    }

    render_slot_svg_open(values, context)
    {
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                style: {
                    'will-change': 'transform',
                    width: 20,
                    height: 20,
                },
                'aria-hidden': true,
                'class': 'bx--navigation-menu-panel-expand-icon',
            })
    }
}
