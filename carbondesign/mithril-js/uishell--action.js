import ProductSwitcher from 'carbon-components/src/components/ui-shell/product-switcher';
import m from 'mithril/hyperscript';
//-
import { Node } from './base';


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
        values.txt_close_menu = "Close menu";
        values.target = vnode.attrs.target;
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': 'bx--header__menu-trigger bx--header__action ' + values['class'],
    'aria-label': values.label,
    title: values.label,
    'data-navigation-menu-panel-label-expand': values.label,
    'data-navigation-menu-panel-label-collapse': values.txt_close_menu,
    'data-product-switcher-target': values.target,
    ...values.props,
  },
  [
    this.slot('svg_open', vnode, values, context),
    this.slot('svg_close', vnode, values, context),
    values.child,
  ])
//##
        );
    }

    render_slot_svg_close(values, context)
    {
        return (
//##
m('svg.bx--navigation-menu-panel-collapse-icon',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    style: {'will-change': 'transform'},
    xmlns: 'http://www.w3.org/2000/svg',
    'aria-hidden': true,
    width: 20,
    height: 20,
    viewBox: '0 0 32 32',
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_slot_svg_open(values, context)
    {
        return (
//##
m('svg.bx--navigation-menu-panel-expand-icon',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    style: {'will-change': 'transform'},
    xmlns: 'http://www.w3.org/2000/svg',
    'aria-hidden': true,
    width: 20,
    height: 20,
    viewBox: '0 0 32 32',
    ...values.props,
  },
  values.child)
//##
        );
    }
}
