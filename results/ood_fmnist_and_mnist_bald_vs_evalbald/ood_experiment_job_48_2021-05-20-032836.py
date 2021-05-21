store = {}
store['timestamp']=1621477716
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=48']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=48
store['worker_id']=48
store['num_workers']=80
store['config']={'seed': 1285, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3052573204040527})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.4647581577301025})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.8551836013793945})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7221899032592773})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.7581958770751953})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6892, 'crossentropy': 2.301052734375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3830828666687012})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4599051475524902})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3909213542938232})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4648287296295166})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 39253], ['id', 53026], ['id', 35450], ['id', 20935], ['id', 38404]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.947573805159909, 1.6008714912121436, 2.066666708371919, 2.3601660922226513, 2.539935789492926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.2739086151123047})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5992395877838135})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.739994525909424})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.975628137588501})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7, 'crossentropy': 1.9189431640625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.393546223640442})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4239633083343506})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.300048589706421})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 8453], ['id', 54757], ['id', 3370], ['id', 14645], ['id', 2156]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8858023517293889, 1.4959576049650294, 1.9745785947170686, 2.3458084949420464, 2.5707526863973182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.008230686187744})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.215672731399536})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.452402353286743})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.09334659576416})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.9053282737731934})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6924, 'crossentropy': 2.1776734375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4886943101882935})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4976367950439453})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.457015037536621})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.406524419784546})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 41078], ['id', 9665], ['id', 11202], ['id', 37231], ['id', 5316]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7763008352369893, 1.4879051865406372, 2.0355625359247327, 2.4292983206938175, 2.691940946114528]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.026437997817993})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.1561479568481445})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.4059200286865234})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.5534496307373047})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.4543204307556152})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7254, 'crossentropy': 1.938534765625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3860507011413574})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3484551906585693})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1982362270355225})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1857821941375732})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 53316], ['id', 11874], ['id', 14256], ['id', 59674], ['id', 26751]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.84282592140825, 1.5908491738280093, 2.0825079962888964, 2.404785659032177, 2.609733021857611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.4474354982376099})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.0034332275390625})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.0170373916625977})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.0924665927886963})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7741, 'crossentropy': 1.35179775390625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0947837829589844})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0485093593597412})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0411304235458374})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 12377], ['id', 50223], ['id', 29300], ['id', 47628], ['id', 28958]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7357516800111956, 1.3506564121966393, 1.8353464335707281, 2.183675390908822, 2.408887532034785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3063559532165527})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7363873720169067})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.7015202045440674})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.7932772636413574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.0123000144958496})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.028125286102295})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.349975109100342})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.22280216217041})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 2.0665206909179688})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.348055601119995})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.2742178440093994})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.3150792121887207})
store['active_learning_steps'][5]['training']['best_epoch']=9
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7748, 'crossentropy': 1.76758671875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1797831058502197})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.116983413696289})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2066295146942139})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.1935982704162598})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1933841705322266})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1300572156906128})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1694345474243164})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0667030811309814})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.1956567764282227})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0916876792907715})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.159911036491394})
store['active_learning_steps'][5]['eval_training']['best_epoch']=8
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 25315], ['id', 59964], ['id', 59725], ['id', 38644], ['id', 10070]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7826461263693967, 1.465789107343321, 1.975383840263123, 2.3554341941375947, 2.628246302064717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.444326400756836})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.7680081129074097})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.8042497634887695})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.144571304321289})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.0758814811706543})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.0732219219207764})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7703, 'crossentropy': 1.76293828125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3135035037994385})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.278870701789856})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.2251412868499756})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.2711913585662842})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.2531802654266357})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 6905], ['id', 55011], ['id', 40259], ['id', 20859], ['id', 56206]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7032455381079052, 1.3048308227366836, 1.7976408211432062, 2.1245423949669666, 2.3563489921549605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.292604923248291})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.440023422241211})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4879378080368042})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6519408226013184})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.658652901649475})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.998178482055664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.9033987522125244})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.7518885135650635})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.821947693824768})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.8932971954345703})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.793761968612671})
store['active_learning_steps'][7]['training']['best_epoch']=8
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8012, 'crossentropy': 1.62949990234375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2461737394332886})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.160799264907837})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.18440580368042})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1738487482070923})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.190291166305542})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 53693], ['id', 23140], ['id', 21981], ['id', 14311], ['id', 25610]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7575353463461794, 1.4360855484408122, 1.935130941588525, 2.3214060396246206, 2.619390846702412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1228123903274536})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1616013050079346})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.3478460311889648})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4041070938110352})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2790906429290771})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5760902166366577})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3916637897491455})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.7305487394332886})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.631168007850647})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.7107727527618408})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6645805835723877})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.815722942352295})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.696274995803833})
store['active_learning_steps'][8]['training']['best_epoch']=10
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8147, 'crossentropy': 1.6722509765625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2235219478607178})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0988290309906006})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.212614893913269})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0990550518035889})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2171106338500977})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.095743179321289})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1032447814941406})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1944305896759033})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.076678991317749})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1358914375305176})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0769295692443848})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.072070598602295})
store['active_learning_steps'][8]['eval_training']['best_epoch']=9
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 24902], ['id', 27412], ['id', 6002], ['id', 56673], ['id', 34780]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8255744028613188, 1.5278785151324774, 2.0817449609610597, 2.4115707772390063, 2.607497285833489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0537914037704468})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0296783447265625})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1024588346481323})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2963333129882812})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.4094347953796387})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3087794780731201})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8289, 'crossentropy': 1.0880359375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9599432945251465})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.941503643989563})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8495250940322876})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9197040796279907})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8695507645606995})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 19124], ['id', 12630], ['id', 21164], ['id', 50910], ['id', 36446]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.639353577999364, 1.2094362967596224, 1.6885059164855685, 2.051936132805169, 2.304531081690735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0633487701416016})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1402509212493896})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2175283432006836})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3467128276824951})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5315362215042114})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5310537815093994})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5076708793640137})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8181, 'crossentropy': 1.14449306640625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0396853685379028})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8954259157180786})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.863917350769043})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.840583324432373})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8294580578804016})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8513907194137573})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 25741], ['id', 20533], ['id', 12836], ['id', 3830], ['id', 4761]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6760794717700886, 1.2288871528846705, 1.6899790905310716, 2.0375142012660294, 2.279543810215745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.130530834197998})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0701898336410522})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1653447151184082})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3394619226455688})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.359523892402649})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.4897509813308716})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.4088337421417236})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4860113859176636})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.52068030834198})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.3802621364593506})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3975900411605835})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.4589965343475342})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.544424295425415})
store['active_learning_steps'][11]['training']['best_epoch']=10
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8488, 'crossentropy': 1.2178025390625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0489630699157715})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.984702467918396})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8997848629951477})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9392757415771484})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9310137033462524})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9513187408447266})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 44961], ['id', 47615], ['id', 29511], ['id', 5155], ['id', 15144]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7575612177948718, 1.409185670327386, 1.9106898938689203, 2.2346899897396915, 2.4215454518220287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.06239914894104})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9540214538574219})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.151053547859192})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3077001571655273})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.381364107131958})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8247, 'crossentropy': 0.98201689453125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1407394409179688})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8532269597053528})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.864883303642273})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8406383991241455})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 31624], ['id', 19298], ['id', 13622], ['id', 45763], ['id', 42472]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.564039979876215, 1.0491459746461622, 1.4511148090779677, 1.748956268399855, 1.9650162092942107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0697546005249023})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.166292667388916})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0996217727661133})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.149939775466919})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.20626962184906})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.268271803855896})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3698911666870117})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.3199806213378906})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8397, 'crossentropy': 1.1263072265625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0481696128845215})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.866374671459198})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8332211375236511})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8179241418838501})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8166669607162476})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 58519], ['id', 58085], ['id', 27431], ['id', 39668], ['id', 43574]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6884409665553493, 1.2825199345504164, 1.742688950595815, 2.105100930133279, 2.3163006227087903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1324868202209473})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9949604272842407})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.059858798980713})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.358506679534912})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.340186595916748})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3648474216461182})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 0.9698775390625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9412335157394409})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7761243581771851})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7514073848724365})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7169522047042847})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7013262510299683})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 13827], ['id', 25281], ['id', 59817], ['id', 12493], ['id', 56044]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6597685043578965, 1.2208881857569036, 1.666926144679639, 2.0218581957110056, 2.2716506748051364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0725457668304443})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8917158842086792})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.966113805770874})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0076420307159424})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0343574285507202})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.148118257522583})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.162994384765625})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8671, 'crossentropy': 0.92505009765625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9694777727127075})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9165071249008179})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8283782005310059})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8145378232002258})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7881968021392822})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7925777435302734})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 46878], ['id', 46447], ['id', 2872], ['id', 27420], ['id', 50878]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6977073100357465, 1.3320387403726808, 1.8366092285974052, 2.1859458915932892, 2.427575960938002]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0108158588409424})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0071948766708374})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0412347316741943})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0714194774627686})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2503662109375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.254564881324768})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2679194211959839})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.849, 'crossentropy': 1.04870166015625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9356781840324402})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9318059682846069})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7999354600906372})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7611920833587646})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7368596792221069})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7074043154716492})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 52661], ['id', 28803], ['id', 28930], ['id', 45268], ['id', 7866]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6802872227738637, 1.2328920337564653, 1.6838953778404049, 2.0487613143893952, 2.330876484641136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8981536626815796})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9144628643989563})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0005619525909424})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1368086338043213})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0337696075439453})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0121515989303589})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1175312995910645})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0931130647659302})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1898488998413086})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8711, 'crossentropy': 0.92055263671875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9299734830856323})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8346339464187622})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7703244686126709})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8081053495407104})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8009963631629944})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7242764234542847})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 30675], ['id', 56495], ['id', 5062], ['id', 5679], ['id', 452]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6712522623833089, 1.2818401906219266, 1.7855145323041726, 2.1848239230889077, 2.462202933684876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9345191121101379})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9741905331611633})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9696226119995117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.950898289680481})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9846962690353394})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2468152046203613})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0755287408828735})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.9574943359375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9746431112289429})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.783684492111206})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7280080318450928})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6503151655197144})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7127602100372314})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6676537990570068})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 13869], ['id', 56316], ['id', 53116], ['id', 29712], ['id', 14171]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.608227224126321, 1.1568793286647643, 1.624151641140688, 1.98108760798966, 2.208701637087265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.966144323348999})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8173378109931946})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9356597661972046})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.043506383895874})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9534587860107422})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1541895866394043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0453276634216309})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.120036244392395})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.998393177986145})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0106616020202637})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2180321216583252})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1172889471054077})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.287229061126709})
store['active_learning_steps'][19]['training']['best_epoch']=10
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8772, 'crossentropy': 0.96473974609375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0599507093429565})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.782318115234375})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7551772594451904})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6676183938980103})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6204231381416321})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.647732675075531})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6136840581893921})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5943863391876221})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6175359487533569})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6485868692398071})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5845893025398254})
store['active_learning_steps'][19]['eval_training']['best_epoch']=8
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 49064], ['id', 5954], ['id', 2126], ['id', 34625], ['id', 31850]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7716535865164904, 1.4425006145684613, 1.9791253127911719, 2.372876215002397, 2.6252775856738833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9287389516830444})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7288488149642944})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7640982866287231})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7743121385574341})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7541595697402954})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0502574443817139})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7859101295471191})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9330748319625854})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8826510906219482})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9752483367919922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0735840797424316})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9680595397949219})
store['active_learning_steps'][20]['training']['best_epoch']=9
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8964, 'crossentropy': 0.823458984375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8609733581542969})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6949111223220825})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6583351492881775})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5843814015388489})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.617751955986023})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6063542366027832})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5535181760787964})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 45017], ['id', 41353], ['id', 39705], ['id', 38785], ['id', 38617]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7312053745438636, 1.3552704926037378, 1.8751886959504924, 2.2283604015517238, 2.440088177787495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9369872808456421})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6552242040634155})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7267036437988281})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6404681205749512})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7116488814353943})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6622542142868042})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9643319845199585})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.634757568359375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8940706253051758})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6157776117324829})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5422535538673401})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5341051816940308})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5688072443008423})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5152591466903687})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 13842], ['id', 7917], ['id', 4066], ['id', 17492], ['id', 32712]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7818264439178149, 1.4404760449809784, 1.9135023016600945, 2.229423167402948, 2.4239436095091422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9390479326248169})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6925396919250488})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7058895826339722})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.781447172164917})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7713065147399902})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7759659290313721})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8122970461845398})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9169950485229492})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7812974452972412})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.754414111328125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.959102213382721})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6574726104736328})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.639479398727417})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6089304685592651})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5308681726455688})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5577539205551147})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5305455923080444})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5039722323417664})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 30144], ['id', 11600], ['id', 41436], ['id', 35996], ['id', 6231]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7643448529140615, 1.3753302688951434, 1.8981672317761493, 2.2756019186189045, 2.48019412213443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8598151206970215})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7450706958770752})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6492129564285278})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7140911221504211})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7121709585189819})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7280627489089966})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8188703656196594})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.612327099609375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9265506267547607})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6036491394042969})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5741915702819824})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5338964462280273})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4929496645927429})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.509871244430542})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 9731], ['id', 15737], ['id', 30883], ['id', 17792], ['id', 38185]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6184228823755427, 1.1541462231667814, 1.5467012385916545, 1.8367089216924173, 2.027608082491601]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9100329875946045})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6580440998077393})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7461051940917969})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6608890295028687})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7079271078109741})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.621595703125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9247920513153076})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6648484468460083})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.616884708404541})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6214537620544434})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 38912], ['id', 21598], ['id', 43796], ['id', 50052], ['id', 31962]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5376356386335415, 1.0532851282841382, 1.4538167923379364, 1.7762225017870463, 2.0233372950692736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8378393650054932})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6385208964347839})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7599983215332031})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6284921169281006})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6537027359008789})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.807445764541626})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7469966411590576})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6463515162467957})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.627762158203125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8876490592956543})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6402988433837891})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6018878221511841})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.547639012336731})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4981469511985779})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.517629861831665})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4652319550514221})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 14825], ['id', 12650], ['id', 37086], ['id', 59681], ['id', 29850]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6776156848881698, 1.2586119965208482, 1.681536834544319, 1.9819665107012963, 2.193589081484772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.956216037273407})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7327679395675659})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.75935959815979})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6563279628753662})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7095911502838135})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7710397243499756})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7014507055282593})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.650033154296875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9044116735458374})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6399121880531311})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5664642453193665})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5218029618263245})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5174667835235596})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.506497859954834})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 51371], ['id', 55496], ['id', 19948], ['id', 42869], ['id', 57540]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6606266921369157, 1.24125026689548, 1.6510701358196718, 1.944818411185409, 2.1422427615160062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8931159973144531})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6102422475814819})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6191461682319641})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6340427994728088})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6073051691055298})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6631491184234619})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6822322607040405})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7002331018447876})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6891951560974121})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8261539936065674})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7637245655059814})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.59127861328125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8330131769180298})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.624935507774353})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5204696655273438})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4842153787612915})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.46031326055526733})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.43988269567489624})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.45282262563705444})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.46485912799835205})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.45302051305770874})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 38275], ['id', 51154], ['id', 42565], ['id', 32277], ['id', 9782]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.641326021003698, 1.2442890139066396, 1.7001107709613192, 2.038530019439845, 2.2773269247064984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9083326458930969})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6437910795211792})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6547880172729492})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6078770160675049})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6208815574645996})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7012723088264465})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6759578585624695})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7515476942062378})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.597928369140625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9352492094039917})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6406468152999878})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5640991926193237})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5354311466217041})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5317052602767944})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4925990104675293})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5045833587646484})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 37078], ['id', 4165], ['id', 37605], ['id', 38053], ['id', 11074]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.648876741836159, 1.1590403862465322, 1.5951230110385435, 1.8969702918077438, 2.110464237095016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.044798731803894})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.786419153213501})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6481924057006836})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6363279819488525})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6590203046798706})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8173735737800598})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.809140682220459})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.58391845703125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9291828870773315})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6465672254562378})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5184928178787231})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.49937212467193604})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5118480324745178})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49409550428390503})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 41295], ['id', 33729], ['id', 15134], ['id', 22083], ['id', 25520]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5842369486268211, 1.1147101540709161, 1.5872999156321588, 1.9565494885710608, 2.1912594466299877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0354321002960205})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6654866337776184})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6506431698799133})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6572551131248474})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.674834132194519})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6386524438858032})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6415016651153564})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6376372575759888})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7692990303039551})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.705751895904541})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.629048779296875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8589701652526855})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.604601263999939})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5545157194137573})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5753158330917358})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5224913358688354})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5442244410514832})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5054506063461304})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.48974961042404175})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 12884], ['id', 14506], ['id', 668], ['id', 5740], ['id', 2513]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5980232889593947, 1.1516629421120732, 1.646887207912128, 1.9981217424685251, 2.2305869982709012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0078799724578857})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6044925451278687})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6232497692108154})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6234689950942993})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5826886296272278})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5584321022033691})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6304104924201965})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6747109889984131})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6131709814071655})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6731885671615601})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7105107307434082})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.567964697265625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8958306312561035})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.622730016708374})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5315974354743958})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4744096100330353})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.46129125356674194})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4625203609466553})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4140830338001251})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.45792943239212036})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4517921805381775})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.44875627756118774})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 37048], ['id', 13374], ['id', 18904], ['id', 35196], ['id', 40448]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6595733296424517, 1.2034453564403527, 1.6915337774360508, 2.0634892271652543, 2.3278841280120823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0446995496749878})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6355242729187012})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.537284255027771})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.596579372882843})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5493149757385254})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5518536567687988})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5927731990814209})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5824992656707764})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5246948599815369})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.608953595161438})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6001513004302979})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6540600061416626})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.513076513671875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9725059866905212})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5654233694076538})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49132394790649414})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47422051429748535})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43988439440727234})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41194427013397217})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40729671716690063})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42312294244766235})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4115632176399231})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4112430810928345})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38402271270751953})
store['active_learning_steps'][32]['eval_training']['best_epoch']=10
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 14619], ['id', 28136], ['id', 13949], ['id', 35043], ['id', 36309]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7354689817679155, 1.3745655427866297, 1.911227335984675, 2.3208536335821135, 2.6243371279528054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1074867248535156})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6820051670074463})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5911345481872559})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5210790634155273})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5840423107147217})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5896860361099243})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6077537536621094})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6030250787734985})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.628132700920105})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6386393904685974})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.50546982421875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.977055549621582})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6523818969726562})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5730596780776978})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.53246009349823})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4854602813720703})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.45226532220840454})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 11621], ['id', 26034], ['id', 56224], ['id', 18840], ['id', 13658]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6278637170648599, 1.2172342889818997, 1.7510874700736307, 2.100586588596522, 2.3765036861678075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0973820686340332})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6284924745559692})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.581511378288269})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5574264526367188})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.576439619064331})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5380124449729919})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5360078811645508})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6229887008666992})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.93, 'crossentropy': 0.473369287109375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0151689052581787})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6444425582885742})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5197476148605347})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.47155267000198364})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43267011642456055})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4550112783908844})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.44875502586364746})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52914], ['id', 48260], ['id', 7574], ['id', 52971], ['id', 48341]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.609186102026521, 1.1413735865418424, 1.598465864247987, 1.9284826157993633, 2.161189357484597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0381979942321777})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6123207807540894})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5800343751907349})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5253697633743286})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6549953818321228})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.644694447517395})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5863305330276489})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6443532705307007})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6557289361953735})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7098832130432129})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.527357470703125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0132791996002197})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6665222644805908})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5240291953086853})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4934728145599365})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4930194616317749})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44684118032455444})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46764257550239563})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4460698068141937})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45704135298728943})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 43897], ['id', 4158], ['id', 35382], ['id', 31339], ['id', 16188]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6552982729560441, 1.2307102200108875, 1.7158162975007833, 2.0001957431519584, 2.1611712164330754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9584226012229919})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6162704229354858})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5580240488052368})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5838204026222229})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5160650014877319})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5787985324859619})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6001406908035278})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.609544038772583})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.481645361328125}
