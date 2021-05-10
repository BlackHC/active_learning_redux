store = {}
store['timestamp']=1620298839
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=24']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=24
store['worker_id']=24
store['num_workers']=40
store['config']={'seed': 28, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.0911107063293457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.5415308475494385})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.2463698387145996})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.712232828140259})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7058, 'crossentropy': 1.9501849609375}
store['active_learning_steps'][0]['acquisition']={'indices': [18009, 57649, 55210, 57381, 27885], 'labels': [9, 2, -1, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.301696300506592})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.592919111251831})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7538962364196777})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8798933029174805})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6898, 'crossentropy': 2.07492109375}
store['active_learning_steps'][1]['acquisition']={'indices': [30549, 53103, 5971, 58966, 37422], 'labels': [7, 1, -1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7841460704803467})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.565258502960205})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.6165289878845215})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.6694273948669434})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.73, 'crossentropy': 1.8123537109375}
store['active_learning_steps'][2]['acquisition']={'indices': [5509, 38313, 18834, 16893, 51703], 'labels': [2, 5, -1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8671592473983765})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.284151554107666})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.075702667236328})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.5466768741607666})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7211, 'crossentropy': 1.64345078125}
store['active_learning_steps'][3]['acquisition']={'indices': [49666, 24946, 22289, 9063, 41802], 'labels': [-1, -1, 8, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.9306331872940063})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.048220157623291})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.4423141479492188})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.258103370666504})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7328, 'crossentropy': 1.6942537109375}
store['active_learning_steps'][4]['acquisition']={'indices': [8921, 7938, 27931, 24742, 28036], 'labels': [2, -1, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.7702089548110962})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.162414073944092})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.2399396896362305})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.2275118827819824})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.761, 'crossentropy': 1.48788486328125}
store['active_learning_steps'][5]['acquisition']={'indices': [31218, 33667, 7330, 40184, 33964], 'labels': [9, 1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.7581764459609985})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.7262752056121826})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.054255962371826})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.0623316764831543})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.263242244720459})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7852, 'crossentropy': 1.50851875}
store['active_learning_steps'][6]['acquisition']={'indices': [3887, 48447, 55670, 48459, 49061], 'labels': [7, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.5341216325759888})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6419190168380737})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 2.0229315757751465})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 2.014448642730713})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7976, 'crossentropy': 1.2145935546875}
store['active_learning_steps'][7]['acquisition']={'indices': [42829, 12169, 18851, 43940, 49200], 'labels': [6, 4, 2, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.306242823600769})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.666301965713501})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6303706169128418})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7611877918243408})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8021, 'crossentropy': 1.0789466796875}
store['active_learning_steps'][8]['acquisition']={'indices': [39269, 48802, 27097, 38694, 7120], 'labels': [4, 9, 4, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.419938564300537})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.5327974557876587})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4339698553085327})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.6979310512542725})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7999, 'crossentropy': 1.29279638671875}
store['active_learning_steps'][9]['acquisition']={'indices': [4312, 33212, 44324, 2707, 4349], 'labels': [5, 9, 1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.3392317295074463})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3193292617797852})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2506600618362427})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.5379915237426758})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5953314304351807})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5912141799926758})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8418, 'crossentropy': 1.0891359375}
store['active_learning_steps'][10]['acquisition']={'indices': [40872, 30156, 40188, 40237, 54420], 'labels': [-1, -1, -1, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1866910457611084})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.4011471271514893})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3092725276947021})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3298372030258179})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8281, 'crossentropy': 1.0128529296875}
store['active_learning_steps'][11]['acquisition']={'indices': [52448, 26524, 21695, 38558, 30940], 'labels': [-1, -1, 3, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1413660049438477})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2530641555786133})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3075499534606934})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.4165620803833008})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8416, 'crossentropy': 0.96482236328125}
store['active_learning_steps'][12]['acquisition']={'indices': [51309, 27851, 3884, 9612, 21764], 'labels': [4, 8, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.193285584449768})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1971681118011475})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.376647710800171})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.4027042388916016})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8185, 'crossentropy': 1.00942060546875}
store['active_learning_steps'][13]['acquisition']={'indices': [50848, 21738, 10206, 49817, 33095], 'labels': [-1, -1, 3, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1331861019134521})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.340036392211914})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4699063301086426})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3860914707183838})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.841, 'crossentropy': 0.9573701171875}
store['active_learning_steps'][14]['acquisition']={'indices': [14065, 38003, 1722, 29769, 28950], 'labels': [3, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.148254156112671})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4093585014343262})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2983076572418213})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.468543529510498})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8253, 'crossentropy': 1.02717978515625}
store['active_learning_steps'][15]['acquisition']={'indices': [19136, 2442, 59232, 36200, 30616], 'labels': [1, -1, 4, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2591779232025146})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2974824905395508})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4953374862670898})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.5262644290924072})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7965, 'crossentropy': 1.09927275390625}
store['active_learning_steps'][16]['acquisition']={'indices': [22000, 36100, 16662, 24949, 16025], 'labels': [3, 2, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2132878303527832})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.499387264251709})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2657008171081543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.4252066612243652})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7827, 'crossentropy': 1.14288583984375}
store['active_learning_steps'][17]['acquisition']={'indices': [48357, 33662, 51590, 34469, 4317], 'labels': [-1, 2, 9, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2344112396240234})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2434009313583374})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3849278688430786})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5825214385986328})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8116, 'crossentropy': 1.0065451171875}
store['active_learning_steps'][18]['acquisition']={'indices': [18007, 2953, 41226, 13012, 34823], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2563855648040771})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.411634922027588})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.6347286701202393})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.508383870124817})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8058, 'crossentropy': 1.0973484375}
store['active_learning_steps'][19]['acquisition']={'indices': [30970, 12894, 25437, 42253, 9627], 'labels': [-1, 9, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2115590572357178})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.263668417930603})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.3644578456878662})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3593199253082275})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8222, 'crossentropy': 1.02521630859375}
store['active_learning_steps'][20]['acquisition']={'indices': [6208, 5288, 34957, 36405, 35136], 'labels': [1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2877888679504395})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3550848960876465})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.468557596206665})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6058077812194824})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7845, 'crossentropy': 1.10154765625}
store['active_learning_steps'][21]['acquisition']={'indices': [37388, 25157, 21918, 37275, 9870], 'labels': [4, 2, -1, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.441151738166809})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5573018789291382})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.5734895467758179})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.9196274280548096})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7806, 'crossentropy': 1.3053146484375}
store['active_learning_steps'][22]['acquisition']={'indices': [47877, 14970, 54794, 36227, 6581], 'labels': [-1, -1, 2, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.3361130952835083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.4653109312057495})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.583963394165039})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5902838706970215})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8084, 'crossentropy': 1.06723388671875}
store['active_learning_steps'][23]['acquisition']={'indices': [9157, 11688, 44248, 29612, 4375], 'labels': [-1, 9, -1, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1031200885772705})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.292123556137085})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.294370412826538})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.4275929927825928})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8276, 'crossentropy': 0.98117119140625}
store['active_learning_steps'][24]['acquisition']={'indices': [13832, 30392, 20638, 55689, 31146], 'labels': [-1, -1, 9, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0465848445892334})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2076653242111206})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.516723394393921})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.499813199043274})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8149, 'crossentropy': 0.97401806640625}
store['active_learning_steps'][25]['acquisition']={'indices': [16923, 6568, 31151, 18041, 31170], 'labels': [1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0947835445404053})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1791574954986572})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.4158573150634766})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3649920225143433})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.81, 'crossentropy': 0.9506294921875}
store['active_learning_steps'][26]['acquisition']={'indices': [31666, 44046, 5660, 4954, 9229], 'labels': [2, -1, 3, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.194250226020813})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2629191875457764})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.407252311706543})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.4684031009674072})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7944, 'crossentropy': 1.1232662109375}
store['active_learning_steps'][27]['acquisition']={'indices': [20572, 18659, 1923, 16917, 35667], 'labels': [6, -1, 2, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0668573379516602})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.360243558883667})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4179556369781494})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3179161548614502})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8281, 'crossentropy': 0.9123328125}
store['active_learning_steps'][28]['acquisition']={'indices': [19811, 58219, 42849, 48820, 33306], 'labels': [-1, 3, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2088438272476196})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.208303689956665})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.338399887084961})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3700389862060547})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.478898286819458})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8494, 'crossentropy': 0.97086884765625}
store['active_learning_steps'][29]['acquisition']={'indices': [26001, 51565, 45082, 54175, 54813], 'labels': [7, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0236504077911377})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0454295873641968})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.190618872642517})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1778228282928467})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8252, 'crossentropy': 0.920281640625}
store['active_learning_steps'][30]['acquisition']={'indices': [54872, 10283, 49059, 49593, 14437], 'labels': [-1, 0, -1, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0511637926101685})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0320181846618652})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.188758373260498})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1538164615631104})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1673097610473633})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8651, 'crossentropy': 0.83888955078125}
store['active_learning_steps'][31]['acquisition']={'indices': [9201, 4043, 14037, 19430, 10512], 'labels': [6, 8, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0620912313461304})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1039466857910156})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2475287914276123})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1082289218902588})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8303, 'crossentropy': 0.8655083984375}
store['active_learning_steps'][32]['acquisition']={'indices': [1394, 36662, 10281, 10051, 49794], 'labels': [1, 2, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0036048889160156})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.09248685836792})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.123354434967041})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3480041027069092})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8265, 'crossentropy': 0.87137958984375}
store['active_learning_steps'][33]['acquisition']={'indices': [39599, 33089, 9813, 14191, 18605], 'labels': [8, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9887664318084717})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.083111047744751})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.325186014175415})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.396985411643982})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8487, 'crossentropy': 0.86173447265625}
store['active_learning_steps'][34]['acquisition']={'indices': [46938, 44061, 12063, 13729, 38457], 'labels': [7, -1, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9910011291503906})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0286004543304443})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1281566619873047})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2588536739349365})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8413, 'crossentropy': 0.8081708984375}
store['active_learning_steps'][35]['acquisition']={'indices': [33029, 58508, 38788, 45751, 14423], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0365384817123413})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.109276533126831})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2120673656463623})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2429955005645752})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8281, 'crossentropy': 0.916737109375}
store['active_learning_steps'][36]['acquisition']={'indices': [29200, 52171, 11219, 26812, 6109], 'labels': [-1, 8, 3, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9374830722808838})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0568829774856567})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0868513584136963})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0878305435180664})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8459, 'crossentropy': 0.805810302734375}
store['active_learning_steps'][37]['acquisition']={'indices': [40259, 50310, 32065, 898, 2503], 'labels': [-1, -1, 2, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.2080121040344238})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.203019618988037})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1946313381195068})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.3732463121414185})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.296592116355896})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.3407588005065918})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8608, 'crossentropy': 0.97791845703125}
store['active_learning_steps'][38]['acquisition']={'indices': [13490, 4758, 30638, 30071, 36072], 'labels': [2, 4, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.029496192932129})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0668081045150757})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1419126987457275})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1449878215789795})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.834, 'crossentropy': 0.86880224609375}
store['active_learning_steps'][39]['acquisition']={'indices': [30807, 24500, 57780, 1052, 20903], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.14834463596344})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.051389455795288})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1682794094085693})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2168806791305542})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.482284426689148})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8537, 'crossentropy': 0.8523171875}
store['active_learning_steps'][40]['acquisition']={'indices': [34763, 17549, 49841, 56984, 30674], 'labels': [8, 0, 3, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8892830610275269})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0611772537231445})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0496015548706055})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0833089351654053})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8589, 'crossentropy': 0.789588623046875}
store['active_learning_steps'][41]['acquisition']={'indices': [12886, 51790, 23739, 55256, 36113], 'labels': [-1, 3, 0, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1654741764068604})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1936264038085938})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1052722930908203})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1075232028961182})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.3122426271438599})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.3025696277618408})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8623, 'crossentropy': 0.93052080078125}
store['active_learning_steps'][42]['acquisition']={'indices': [44841, 51056, 57737, 9894, 33844], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8952630758285522})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9545239806175232})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0736234188079834})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1631790399551392})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8397, 'crossentropy': 0.8429091796875}
store['active_learning_steps'][43]['acquisition']={'indices': [54440, 29824, 36998, 31766, 33214], 'labels': [-1, 9, 2, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9297774434089661})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9444917440414429})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1387261152267456})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1745959520339966})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8385, 'crossentropy': 0.84420966796875}
store['active_learning_steps'][44]['acquisition']={'indices': [891, 52761, 29715, 29065, 56948], 'labels': [1, 9, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9226667881011963})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9100876450538635})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0339174270629883})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.1209442615509033})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2900410890579224})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.865, 'crossentropy': 0.783167724609375}
store['active_learning_steps'][45]['acquisition']={'indices': [57778, 15038, 8852, 29883, 29552], 'labels': [1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9133381843566895})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9690288305282593})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.042486310005188})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1840991973876953})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8446, 'crossentropy': 0.82806025390625}
store['active_learning_steps'][46]['acquisition']={'indices': [15939, 28045, 26899, 35690, 12623], 'labels': [7, 8, 2, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9981392621994019})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9129557609558105})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0397741794586182})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1135811805725098})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1463065147399902})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8715, 'crossentropy': 0.778953466796875}
store['active_learning_steps'][47]['acquisition']={'indices': [288, 48244, 13910, 1782, 35209], 'labels': [7, 9, 2, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9007126092910767})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0012784004211426})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0811172723770142})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0736298561096191})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8376, 'crossentropy': 0.83818125}
store['active_learning_steps'][48]['acquisition']={'indices': [43011, 49271, 31050, 31582, 55084], 'labels': [-1, 4, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9708107113838196})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8782720565795898})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9279480576515198})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.029470443725586})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1351954936981201})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.88, 'crossentropy': 0.720167724609375}
store['active_learning_steps'][49]['acquisition']={'indices': [7548, 29047, 32121, 6933, 6338], 'labels': [-1, 4, 9, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8893393278121948})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.036851167678833})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9245002269744873})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1176519393920898})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8445, 'crossentropy': 0.80193408203125}
store['active_learning_steps'][50]['acquisition']={'indices': [56224, 52809, 46230, 19148, 43303], 'labels': [5, 0, 4, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9090217351913452})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8378629088401794})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8438515663146973})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9544668793678284})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9551274180412292})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.70981884765625}
store['active_learning_steps'][51]['acquisition']={'indices': [6698, 29334, 24268, 51216, 30261], 'labels': [1, 2, -1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9595232009887695})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.810914933681488})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0347150564193726})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9503294229507446})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0056872367858887})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.69922626953125}
store['active_learning_steps'][52]['acquisition']={'indices': [31709, 33237, 30422, 5651, 30109], 'labels': [2, 0, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8992952108383179})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9372631311416626})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0640232563018799})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1067376136779785})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8537, 'crossentropy': 0.78133779296875}
store['active_learning_steps'][53]['acquisition']={'indices': [26111, 38108, 56286, 45537, 45146], 'labels': [4, 2, 8, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8324801921844482})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8548651933670044})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0195988416671753})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9344099760055542})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8652, 'crossentropy': 0.715326318359375}
store['active_learning_steps'][54]['acquisition']={'indices': [35594, 50825, 14489, 38242, 4028], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8862539529800415})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8586660027503967})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9892517328262329})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9648306369781494})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9433484077453613})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.67982041015625}
store['active_learning_steps'][55]['acquisition']={'indices': [4841, 341, 22309, 46477, 23023], 'labels': [6, 3, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9155364036560059})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8747890591621399})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9867537021636963})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0373320579528809})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9715577363967896})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.74061611328125}
store['active_learning_steps'][56]['acquisition']={'indices': [7287, 3886, 38944, 22364, 5056], 'labels': [7, 2, -1, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9274266958236694})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.786562442779541})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7928906083106995})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9182091355323792})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0611519813537598})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8906, 'crossentropy': 0.63438857421875}
store['active_learning_steps'][57]['acquisition']={'indices': [41154, 17114, 23581, 17109, 47062], 'labels': [-1, -1, 3, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8731926083564758})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8450124263763428})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8649641275405884})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9061554670333862})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8805255889892578})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8823, 'crossentropy': 0.739550341796875}
store['active_learning_steps'][58]['acquisition']={'indices': [1144, 57534, 39783, 44, 19247], 'labels': [-1, 7, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8199699521064758})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9608210325241089})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8904141783714294})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8195422887802124})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9345729351043701})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9320688247680664})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0489689111709595})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.691329638671875}
store['active_learning_steps'][59]['acquisition']={'indices': [8857, 8730, 25743, 11831, 27046], 'labels': [4, -1, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8222023844718933})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7274755239486694})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7259854674339294})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7828524112701416})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8252005577087402})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7935491800308228})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.59724326171875}
store['active_learning_steps'][60]['acquisition']={'indices': [57176, 19373, 1375, 54641, 45864], 'labels': [-1, 2, 1, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8029453158378601})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7020388841629028})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.855016827583313})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8006483316421509})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.816990077495575})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.62668974609375}
store['active_learning_steps'][61]['acquisition']={'indices': [51988, 38344, 10261, 43391, 8147], 'labels': [7, 9, 0, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7919355034828186})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7675661444664001})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7206165790557861})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7306951284408569})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7232906818389893})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8709045052528381})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9064, 'crossentropy': 0.6002458984375}
store['active_learning_steps'][62]['acquisition']={'indices': [3202, 36195, 28175, 59891, 27865], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7900293469429016})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7449731230735779})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7136948108673096})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.796120285987854})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7364059686660767})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8228338956832886})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8966, 'crossentropy': 0.63380146484375}
store['active_learning_steps'][63]['acquisition']={'indices': [52646, 50154, 59116, 47205, 7014], 'labels': [9, 4, 1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7776929140090942})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7960487604141235})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7087656855583191})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8042358160018921})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8212067484855652})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.808789849281311})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.902, 'crossentropy': 0.66332861328125}
store['active_learning_steps'][64]['acquisition']={'indices': [31368, 13029, 28546, 4178, 30837], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8134844303131104})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.640900731086731})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6822971105575562})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7124574780464172})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7668245434761047})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.567714794921875}
store['active_learning_steps'][65]['acquisition']={'indices': [5731, 21707, 43283, 27683, 40595], 'labels': [-1, 5, 0, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7253986597061157})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.685623824596405})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6862800121307373})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7181153297424316})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7055279016494751})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.571780322265625}
store['active_learning_steps'][66]['acquisition']={'indices': [8799, 43027, 45525, 57703, 25006], 'labels': [6, 3, 9, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7733703851699829})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6238391995429993})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6785067319869995})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.737827479839325})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6549896597862244})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.5796708984375}
store['active_learning_steps'][67]['acquisition']={'indices': [59443, 8287, 26497, 78, 3110], 'labels': [-1, 9, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7370707988739014})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7197616100311279})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6594179272651672})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6646517515182495})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6772952079772949})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6733474731445312})
store['active_learning_steps'][68]['training']['best_epoch']=3
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.599374609375}
store['active_learning_steps'][68]['acquisition']={'indices': [997, 41515, 2241, 57584, 49715], 'labels': [0, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.851513683795929})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6541448831558228})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7008751630783081})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6810324192047119})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7462235689163208})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9021, 'crossentropy': 0.62553330078125}
store['active_learning_steps'][69]['acquisition']={'indices': [15449, 13693, 21720, 34082, 59169], 'labels': [7, 2, 3, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8006341457366943})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7848560810089111})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7599793672561646})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8129611015319824})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7631102800369263})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7872116565704346})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9023, 'crossentropy': 0.638831689453125}
store['active_learning_steps'][70]['acquisition']={'indices': [26821, 12181, 13632, 59212, 170], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7764557600021362})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7076312303543091})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7345713973045349})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7293482422828674})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6640669107437134})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6697756052017212})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8809144496917725})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.747655987739563})
store['active_learning_steps'][71]['training']['best_epoch']=5
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9132, 'crossentropy': 0.65488076171875}
store['active_learning_steps'][71]['acquisition']={'indices': [32069, 26042, 42215, 8768, 32392], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7281861305236816})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5788913369178772})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6189085245132446})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6072045564651489})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7146695852279663})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.537708935546875}
store['active_learning_steps'][72]['acquisition']={'indices': [25969, 21307, 51713, 23296, 34102], 'labels': [-1, 4, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8145626783370972})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6693434715270996})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6563308238983154})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6604390144348145})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7142930626869202})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7560651302337646})
store['active_learning_steps'][73]['training']['best_epoch']=3
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.57464619140625}
store['active_learning_steps'][73]['acquisition']={'indices': [54072, 26609, 45964, 37324, 44560], 'labels': [-1, -1, 2, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8222049474716187})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7044907808303833})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6225505471229553})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6577224731445312})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6305394172668457})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6479103565216064})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.508823486328125}
store['active_learning_steps'][74]['acquisition']={'indices': [11100, 1560, 3079, 15645, 24401], 'labels': [-1, -1, -1, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7179880142211914})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.607747495174408})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.615436851978302})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6658726930618286})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6472289562225342})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.5611921875}
store['active_learning_steps'][75]['acquisition']={'indices': [2222, 8962, 10995, 45675, 47921], 'labels': [4, 4, 5, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8345462083816528})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6160925626754761})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.597991943359375})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6133137345314026})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6308614015579224})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7154427170753479})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.530772998046875}
store['active_learning_steps'][76]['acquisition']={'indices': [16302, 3445, 59039, 1671, 18922], 'labels': [4, 6, -1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6620289087295532})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5912082195281982})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5941976308822632})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6948705911636353})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6090922355651855})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.54315107421875}
store['active_learning_steps'][77]['acquisition']={'indices': [31267, 50889, 46971, 3213, 3504], 'labels': [2, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.731167197227478})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6316155195236206})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6062783598899841})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6673568487167358})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6446585059165955})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5925427675247192})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6697624921798706})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7774567008018494})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7333441376686096})
store['active_learning_steps'][78]['training']['best_epoch']=6
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.542514697265625}
store['active_learning_steps'][78]['acquisition']={'indices': [32572, 46438, 15834, 46325, 11886], 'labels': [6, 0, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6675540804862976})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6093467473983765})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6149075031280518})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6126179099082947})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6111869812011719})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.55148701171875}
store['active_learning_steps'][79]['acquisition']={'indices': [14778, 30275, 35755, 22075, 59746], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7453336119651794})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.667582631111145})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6474272608757019})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6968446373939514})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6785525679588318})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7188819646835327})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.59676162109375}
store['active_learning_steps'][80]['acquisition']={'indices': [33675, 53987, 5846, 14280, 21911], 'labels': [-1, 3, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7065069675445557})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5364328622817993})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.576373815536499})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6378062963485718})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6093771457672119})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.520087744140625}
store['active_learning_steps'][81]['acquisition']={'indices': [27589, 19916, 56603, 21450, 23515], 'labels': [-1, -1, 1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7229520082473755})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6681797504425049})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6714280247688293})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5306814312934875})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6059176921844482})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6666014194488525})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6384135484695435})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.516916455078125}
store['active_learning_steps'][82]['acquisition']={'indices': [57888, 9743, 17365, 31082, 16631], 'labels': [1, 5, -1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.707897424697876})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.674285888671875})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6145888566970825})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.608401358127594})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6904784440994263})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6812325119972229})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6581534147262573})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.53156455078125}
store['active_learning_steps'][83]['acquisition']={'indices': [48019, 19195, 59362, 5328, 57095], 'labels': [-1, 3, 9, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6626203060150146})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5396524667739868})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5920542478561401})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5614515542984009})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6156927347183228})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.518669873046875}
store['active_learning_steps'][84]['acquisition']={'indices': [39282, 42686, 37690, 21973, 32900], 'labels': [2, -1, 3, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6976204514503479})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6369040012359619})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6395405530929565})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.70648193359375})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7129917144775391})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.577163818359375}
store['active_learning_steps'][85]['acquisition']={'indices': [3629, 23958, 53589, 17705, 41271], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7024083137512207})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.614294171333313})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5955091714859009})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5770859718322754})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6131778955459595})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6727052927017212})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6979650259017944})
store['active_learning_steps'][86]['training']['best_epoch']=4
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.507964599609375}
store['active_learning_steps'][86]['acquisition']={'indices': [40484, 8654, 5110, 23256, 46690], 'labels': [6, 9, -1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6786458492279053})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5704034566879272})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6141132116317749})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6054661273956299})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5878012180328369})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.505112353515625}
store['active_learning_steps'][87]['acquisition']={'indices': [27630, 25967, 25713, 23013, 37144], 'labels': [1, -1, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8191732168197632})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5421529412269592})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6189395189285278})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5957016348838806})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5756335854530334})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.5515404296875}
store['active_learning_steps'][88]['acquisition']={'indices': [32877, 58876, 11716, 57845, 20115], 'labels': [7, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6661101579666138})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5872352719306946})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.570551872253418})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5498684048652649})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.547057569026947})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5809867978096008})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5694664716720581})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6465228199958801})
store['active_learning_steps'][89]['training']['best_epoch']=5
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.5099283203125}
store['active_learning_steps'][89]['acquisition']={'indices': [3140, 27471, 38458, 29988, 32479], 'labels': [-1, -1, 7, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7753094434738159})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6172577738761902})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5436066389083862})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6765493154525757})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6091489791870117})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6342290639877319})
store['active_learning_steps'][90]['training']['best_epoch']=3
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.4850830078125}
store['active_learning_steps'][90]['acquisition']={'indices': [59849, 18741, 23223, 13433, 35668], 'labels': [-1, 1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7246091365814209})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.633613109588623})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5903520584106445})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5887287259101868})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6264282464981079})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7033880949020386})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6252460479736328})
store['active_learning_steps'][91]['training']['best_epoch']=4
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.48975185546875}
store['active_learning_steps'][91]['acquisition']={'indices': [30847, 26688, 55484, 16398, 15307], 'labels': [-1, 2, 0, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7103423476219177})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.603301465511322})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5292789340019226})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5774011015892029})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5543881058692932})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5811903476715088})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.440219580078125}
store['active_learning_steps'][92]['acquisition']={'indices': [13184, 32708, 57125, 18410, 52908], 'labels': [0, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7123672962188721})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6119892597198486})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5469244718551636})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6051720380783081})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5915061235427856})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5970591306686401})
store['active_learning_steps'][93]['training']['best_epoch']=3
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.500528515625}
store['active_learning_steps'][93]['acquisition']={'indices': [21678, 55200, 23033, 55557, 14314], 'labels': [5, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8114821910858154})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6476409435272217})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5915699005126953})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.562804102897644})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6284366250038147})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6078237891197205})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6699371337890625})
store['active_learning_steps'][94]['training']['best_epoch']=4
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.503928271484375}
store['active_learning_steps'][94]['acquisition']={'indices': [19678, 43063, 42455, 30214, 31988], 'labels': [6, -1, -1, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7129647135734558})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6286109685897827})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6111949682235718})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6143389344215393})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6580160856246948})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5862900614738464})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6346542835235596})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6714550852775574})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6839827299118042})
store['active_learning_steps'][95]['training']['best_epoch']=6
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.569548095703125}
store['active_learning_steps'][95]['acquisition']={'indices': [2070, 20843, 9333, 19967, 53510], 'labels': [8, 0, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7630685567855835})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6106671094894409})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5189569592475891})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6661452054977417})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6098237037658691})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6499960422515869})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.49202333984375}
store['active_learning_steps'][96]['acquisition']={'indices': [6593, 15279, 36182, 1534, 59920], 'labels': [0, 2, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6700292825698853})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5416152477264404})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5653067827224731})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5561679601669312})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5715845823287964})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.4925603515625}
store['active_learning_steps'][97]['acquisition']={'indices': [12262, 18190, 37906, 20747, 55673], 'labels': [6, -1, 9, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6663182377815247})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6139448881149292})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5467250347137451})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6111335754394531})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5648276209831238})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5880093574523926})
store['active_learning_steps'][98]['training']['best_epoch']=3
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.479137451171875}
store['active_learning_steps'][98]['acquisition']={'indices': [11220, 16728, 16173, 49033, 26922], 'labels': [7, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7495874166488647})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6664527654647827})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5555462837219238})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5561186075210571})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7307438254356384})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5756988525390625})
store['active_learning_steps'][99]['training']['best_epoch']=3
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.480811962890625}
store['active_learning_steps'][99]['acquisition']={'indices': [17650, 49591, 4186, 25713, 9592], 'labels': [1, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7403383255004883})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.587005615234375})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5418341159820557})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5829235315322876})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6411974430084229})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5790755748748779})
store['active_learning_steps'][100]['training']['best_epoch']=3
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.487629248046875}
store['active_learning_steps'][100]['acquisition']={'indices': [50266, 29556, 33967, 10582, 7163], 'labels': [6, 1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7029167413711548})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5635184049606323})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6152934432029724})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5465136170387268})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5686739683151245})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5882565379142761})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6056022644042969})
store['active_learning_steps'][101]['training']['best_epoch']=4
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.471564794921875}
store['active_learning_steps'][101]['acquisition']={'indices': [20873, 59635, 45424, 50763, 39493], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7150178551673889})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.58556067943573})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5412864685058594})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.576224684715271})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5620839595794678})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6515206098556519})
store['active_learning_steps'][102]['training']['best_epoch']=3
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.49273505859375}
store['active_learning_steps'][102]['acquisition']={'indices': [50176, 40520, 22031, 21777, 52414], 'labels': [8, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7642043828964233})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5569458603858948})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5664583444595337})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5971038341522217})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7316263914108276})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.499737255859375}
store['active_learning_steps'][103]['acquisition']={'indices': [7271, 32335, 5052, 35546, 9037], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7061053514480591})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.558864176273346})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6323200464248657})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5565166473388672})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5676358342170715})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5248592495918274})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5797642469406128})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5933229923248291})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.570645809173584})
store['active_learning_steps'][104]['training']['best_epoch']=6
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.51690498046875}
store['active_learning_steps'][104]['acquisition']={'indices': [56140, 44150, 35317, 37687, 32415], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6993238925933838})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5673753023147583})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5795469284057617})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5803277492523193})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5907975435256958})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.533120849609375}
store['active_learning_steps'][105]['acquisition']={'indices': [34791, 28098, 27656, 12219, 27139], 'labels': [6, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6902978420257568})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5758350491523743})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5871353149414062})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5574111342430115})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5781946182250977})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5614438652992249})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6275854110717773})
store['active_learning_steps'][106]['training']['best_epoch']=4
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.475368994140625}
store['active_learning_steps'][106]['acquisition']={'indices': [16922, 39375, 59966, 10424, 29423], 'labels': [3, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7119051218032837})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6122514605522156})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5416533946990967})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5617233514785767})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5705427527427673})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5155705809593201})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5347307920455933})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5605837106704712})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6501824855804443})
store['active_learning_steps'][107]['training']['best_epoch']=6
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9372, 'crossentropy': 0.45463271484375}
store['active_learning_steps'][107]['acquisition']={'indices': [21724, 45619, 24112, 6921, 11469], 'labels': [9, 3, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7398132085800171})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5525224208831787})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5328553318977356})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5576714277267456})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5999628305435181})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6011278033256531})
store['active_learning_steps'][108]['training']['best_epoch']=3
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.486164013671875}
store['active_learning_steps'][108]['acquisition']={'indices': [49008, 30008, 30431, 59724, 53263], 'labels': [-1, -1, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6495538949966431})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5903444290161133})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.560100793838501})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5621602535247803})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5341517329216003})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6036579608917236})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5715857744216919})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5577269792556763})
store['active_learning_steps'][109]['training']['best_epoch']=5
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.4837216796875}
store['active_learning_steps'][109]['acquisition']={'indices': [27552, 4679, 51276, 39600, 167], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6824716329574585})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5850305557250977})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5733319520950317})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5329811573028564})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5717521905899048})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6270830631256104})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6171600818634033})
store['active_learning_steps'][110]['training']['best_epoch']=4
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.455560791015625}
store['active_learning_steps'][110]['acquisition']={'indices': [36136, 56674, 12729, 32095, 6539], 'labels': [7, 0, 3, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7568767666816711})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6116353869438171})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5769285559654236})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5482915639877319})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.654942512512207})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5924879908561707})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5788325071334839})
store['active_learning_steps'][111]['training']['best_epoch']=4
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.4724263671875}
store['active_learning_steps'][111]['acquisition']={'indices': [52338, 53684, 57210, 52670, 534], 'labels': [-1, -1, 8, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8245537281036377})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5661251544952393})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5923943519592285})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.647816002368927})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6368565559387207})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.54141728515625}
store['active_learning_steps'][112]['acquisition']={'indices': [30831, 44602, 3806, 3029, 13627], 'labels': [-1, 6, 0, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6658346652984619})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6143630743026733})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5272610187530518})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5597031712532043})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5642639994621277})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.541922926902771})
store['active_learning_steps'][113]['training']['best_epoch']=3
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.463148193359375}
store['active_learning_steps'][113]['acquisition']={'indices': [52444, 47360, 24594, 58649, 34780], 'labels': [-1, 1, 9, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.67998868227005})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5861238837242126})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.539318323135376})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5683275461196899})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5452725887298584})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6437913775444031})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.490744970703125}
store['active_learning_steps'][114]['acquisition']={'indices': [18568, 5086, 19517, 13586, 20818], 'labels': [1, -1, 1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.67304527759552})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5532864332199097})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6136415004730225})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5386393666267395})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5184638500213623})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5408347249031067})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6263270378112793})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5430799722671509})
store['active_learning_steps'][115]['training']['best_epoch']=5
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.474557666015625}
store['active_learning_steps'][115]['acquisition']={'indices': [47727, 58728, 27577, 17199, 4760], 'labels': [-1, -1, 7, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6879702210426331})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6130002737045288})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.524963915348053})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6417521238327026})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5514242649078369})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6262509822845459})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.47696806640625}
store['active_learning_steps'][116]['acquisition']={'indices': [57490, 18192, 6832, 50901, 28629], 'labels': [6, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.738767147064209})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5601750612258911})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6111940145492554})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5174839496612549})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5142972469329834})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5479917526245117})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5615729093551636})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5252531170845032})
store['active_learning_steps'][117]['training']['best_epoch']=5
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.46901455078125}
store['active_learning_steps'][117]['acquisition']={'indices': [48725, 52685, 21337, 42972, 21385], 'labels': [-1, 6, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7049985527992249})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5275474786758423})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6010802984237671})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5682228207588196})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6075616478919983})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.486590478515625}
store['active_learning_steps'][118]['acquisition']={'indices': [25071, 3487, 39006, 23221, 57292], 'labels': [3, 1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6906964778900146})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.601876974105835})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5733766555786133})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5585530996322632})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5938243865966797})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6019072532653809})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.623995304107666})
store['active_learning_steps'][119]['training']['best_epoch']=4
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.470260595703125}
store['active_learning_steps'][119]['acquisition']={'indices': [47496, 7226, 38133, 25013, 9756], 'labels': [3, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6498856544494629})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5707888603210449})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.558796226978302})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5875617265701294})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49734577536582947})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.564605712890625})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5371058583259583})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6240900754928589})
store['active_learning_steps'][120]['training']['best_epoch']=5
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.446775927734375}
store['active_learning_steps'][120]['acquisition']={'indices': [13232, 19812, 34145, 4126, 51678], 'labels': [5, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6718709468841553})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49591904878616333})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5374194383621216})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4911631941795349})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5438778400421143})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5887329578399658})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5025221109390259})
store['active_learning_steps'][121]['training']['best_epoch']=4
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.496340771484375}
store['active_learning_steps'][121]['acquisition']={'indices': [22440, 18564, 42381, 44002, 38711], 'labels': [0, 0, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7257940769195557})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5482580065727234})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49938371777534485})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5049723386764526})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5127826929092407})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5356903076171875})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.466857568359375}
store['active_learning_steps'][122]['acquisition']={'indices': [11342, 13471, 36168, 6604, 6796], 'labels': [1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7134805917739868})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6121882200241089})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5859427452087402})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5643548965454102})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5605604648590088})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6312062740325928})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6396948099136353})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6638017296791077})
store['active_learning_steps'][123]['training']['best_epoch']=5
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.473550244140625}
store['active_learning_steps'][123]['acquisition']={'indices': [16271, 39289, 57627, 40091, 58377], 'labels': [7, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.768338680267334})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.701946496963501})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5969738960266113})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5574116706848145})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5713750123977661})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6948971748352051})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6351187229156494})
store['active_learning_steps'][124]['training']['best_epoch']=4
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.492115625}
store['active_learning_steps'][124]['acquisition']={'indices': [23224, 42866, 7941, 47836, 2986], 'labels': [9, 2, 1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7370918989181519})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6065605282783508})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5446982979774475})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5345864295959473})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5892962217330933})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6390409469604492})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5802593231201172})
store['active_learning_steps'][125]['training']['best_epoch']=4
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.50032197265625}
store['active_learning_steps'][125]['acquisition']={'indices': [17178, 25769, 5879, 20700, 37021], 'labels': [8, 6, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8036743402481079})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5568315982818604})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6123026609420776})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5562775135040283})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5267306566238403})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5738435387611389})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5833113789558411})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5998567342758179})
store['active_learning_steps'][126]['training']['best_epoch']=5
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.4967076171875}
store['active_learning_steps'][126]['acquisition']={'indices': [54030, 10443, 30265, 49081, 19336], 'labels': [8, -1, 3, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7254143357276917})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5460377931594849})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5211786031723022})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5661022663116455})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.477977991104126})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5272620916366577})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6089914441108704})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5593098402023315})
store['active_learning_steps'][127]['training']['best_epoch']=5
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.491402734375}
store['active_learning_steps'][127]['acquisition']={'indices': [18299, 53384, 47937, 1431, 2780], 'labels': [3, 4, 4, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.635124683380127})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5380452871322632})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5387524366378784})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5477255582809448})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5379075407981873})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5349141955375671})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5889052152633667})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6096039414405823})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5561937093734741})
store['active_learning_steps'][128]['training']['best_epoch']=6
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9373, 'crossentropy': 0.477089453125}
store['active_learning_steps'][128]['acquisition']={'indices': [40902, 27446, 693, 38492, 21802], 'labels': [5, -1, 2, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7681931257247925})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6083090305328369})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5547131896018982})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5947251915931702})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5837770700454712})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6132755279541016})
store['active_learning_steps'][129]['training']['best_epoch']=3
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.492675537109375}
store['active_learning_steps'][129]['acquisition']={'indices': [36046, 11160, 9774, 648, 35708], 'labels': [-1, 8, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7470852732658386})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.568642795085907})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5748405456542969})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5544028282165527})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5521110892295837})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5451904535293579})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5766507983207703})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6008912324905396})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6206129193305969})
store['active_learning_steps'][130]['training']['best_epoch']=6
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.448838427734375}
store['active_learning_steps'][130]['acquisition']={'indices': [25956, 44440, 53196, 5641, 42681], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7505103349685669})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5372581481933594})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5372307300567627})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5670884251594543})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5756240487098694})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6012223958969116})
store['active_learning_steps'][131]['training']['best_epoch']=3
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.505365673828125}
store['active_learning_steps'][131]['acquisition']={'indices': [15279, 690, 9541, 12944, 19344], 'labels': [-1, -1, 4, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6601558923721313})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5956929326057434})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.552754282951355})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5444732904434204})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49636441469192505})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5448547005653381})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5248156785964966})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5538595914840698})
store['active_learning_steps'][132]['training']['best_epoch']=5
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.938, 'crossentropy': 0.468689208984375}
store['active_learning_steps'][132]['acquisition']={'indices': [32018, 19548, 44078, 40439, 25954], 'labels': [8, 3, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6847527027130127})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.522116482257843})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5217620730400085})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5080278515815735})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5141341686248779})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5074290633201599})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5229296684265137})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5421018600463867})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48088228702545166})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5593550205230713})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5202891230583191})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5231411457061768})
store['active_learning_steps'][133]['training']['best_epoch']=9
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9435, 'crossentropy': 0.443847412109375}
store['active_learning_steps'][133]['acquisition']={'indices': [59638, 46654, 51997, 34175, 45663], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6950756311416626})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5439881086349487})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4948674738407135})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5318428874015808})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5115981101989746})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4722440242767334})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5070697069168091})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.510020911693573})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6146448850631714})
store['active_learning_steps'][134]['training']['best_epoch']=6
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9442, 'crossentropy': 0.432736669921875}
store['active_learning_steps'][134]['acquisition']={'indices': [38435, 11391, 59801, 30582, 31687], 'labels': [2, 0, -1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.696058452129364})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5202845931053162})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4745696485042572})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.46017181873321533})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49587175250053406})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47268950939178467})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5339011549949646})
store['active_learning_steps'][135]['training']['best_epoch']=4
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9366, 'crossentropy': 0.40558408203125}
store['active_learning_steps'][135]['acquisition']={'indices': [26853, 32711, 178, 20605, 36415], 'labels': [-1, 5, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6998473405838013})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5185743570327759})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49183928966522217})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5000910758972168})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49801820516586304})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5458632707595825})
store['active_learning_steps'][136]['training']['best_epoch']=3
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.44742080078125}
store['active_learning_steps'][136]['acquisition']={'indices': [17732, 43847, 44440, 17603, 39176], 'labels': [5, 0, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7561421394348145})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.544628381729126})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5195615887641907})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5726978182792664})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5483137965202332})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5546129941940308})
store['active_learning_steps'][137]['training']['best_epoch']=3
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.471209716796875}
store['active_learning_steps'][137]['acquisition']={'indices': [19953, 28494, 15940, 44317, 48365], 'labels': [9, 2, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6767905354499817})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5251174569129944})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48730602860450745})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4447619915008545})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5276210308074951})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5474640130996704})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4870202839374542})
store['active_learning_steps'][138]['training']['best_epoch']=4
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9359, 'crossentropy': 0.4366595703125}
store['active_learning_steps'][138]['acquisition']={'indices': [40558, 55765, 25459, 21737, 22568], 'labels': [8, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7235907316207886})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5627678632736206})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.479617714881897})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.541989266872406})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4659106135368347})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48025214672088623})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4667069911956787})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49103015661239624})
store['active_learning_steps'][139]['training']['best_epoch']=5
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.422927880859375}
store['active_learning_steps'][139]['acquisition']={'indices': [15398, 55193, 6563, 24271, 6044], 'labels': [-1, -1, 8, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6076536178588867})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4830173850059509})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5021489858627319})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47299954295158386})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48220282793045044})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4950066804885864})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49599987268447876})
store['active_learning_steps'][140]['training']['best_epoch']=4
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9378, 'crossentropy': 0.44433232421875}
store['active_learning_steps'][140]['acquisition']={'indices': [46376, 38519, 33174, 16849, 28102], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7166240215301514})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49133703112602234})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48923274874687195})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.47897544503211975})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.543319046497345})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4984610080718994})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5235401391983032})
store['active_learning_steps'][141]['training']['best_epoch']=4
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.44510556640625}
store['active_learning_steps'][141]['acquisition']={'indices': [24367, 7100, 13376, 28013, 39050], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6864662170410156})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.631752610206604})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49279171228408813})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.523756206035614})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.517890989780426})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5504095554351807})
store['active_learning_steps'][142]['training']['best_epoch']=3
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.43639384765625}
store['active_learning_steps'][142]['acquisition']={'indices': [21632, 52220, 32826, 6431, 6268], 'labels': [5, 1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6667994260787964})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.533341646194458})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48618441820144653})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4924560785293579})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.438541054725647})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5274497270584106})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.530123770236969})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.611264705657959})
store['active_learning_steps'][143]['training']['best_epoch']=5
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.43910302734375}
store['active_learning_steps'][143]['acquisition']={'indices': [20254, 50928, 36695, 20276, 30020], 'labels': [-1, 1, 5, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6778192520141602})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.554445207118988})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48285549879074097})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5816307663917542})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48099440336227417})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5401772856712341})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48481935262680054})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5176529884338379})
store['active_learning_steps'][144]['training']['best_epoch']=5
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.4602611328125}
store['active_learning_steps'][144]['acquisition']={'indices': [40711, 5127, 41752, 54374, 46114], 'labels': [5, 3, 5, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.717188835144043})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5860267877578735})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4767189919948578})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5272954702377319})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5210683345794678})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5199493169784546})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.453174853515625}
store['active_learning_steps'][145]['acquisition']={'indices': [54925, 45016, 25971, 40798, 55547], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7195706367492676})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.546600341796875})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.501386284828186})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49380743503570557})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5641418695449829})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49349623918533325})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4640434980392456})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4737492501735687})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5185557007789612})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5052556395530701})
store['active_learning_steps'][146]['training']['best_epoch']=7
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9433, 'crossentropy': 0.43103828125}
store['active_learning_steps'][146]['acquisition']={'indices': [32162, 24448, 23872, 47077, 45558], 'labels': [0, -1, 1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6410415172576904})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5022454857826233})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45603886246681213})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4579184651374817})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4593145549297333})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47620290517807007})
store['active_learning_steps'][147]['training']['best_epoch']=3
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.4057107666015625}
store['active_learning_steps'][147]['acquisition']={'indices': [44727, 14207, 2965, 43657, 39130], 'labels': [2, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6936444044113159})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5317586064338684})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5055804252624512})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48067960143089294})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4472927451133728})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5242658853530884})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48961204290390015})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5467990636825562})
store['active_learning_steps'][148]['training']['best_epoch']=5
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.419221826171875}
store['active_learning_steps'][148]['acquisition']={'indices': [39690, 57152, 45230, 9052, 24226], 'labels': [4, 9, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6548976898193359})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5263630151748657})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5096486806869507})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5180028080940247})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5356618165969849})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5366599559783936})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.4526416015625}
store['active_learning_steps'][149]['acquisition']={'indices': [26209, 55371, 20967, 40916, 21677], 'labels': [-1, 1, 2, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6923890113830566})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.535637617111206})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4960566759109497})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4893496632575989})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43534696102142334})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4825966954231262})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5277369618415833})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5353551506996155})
store['active_learning_steps'][150]['training']['best_epoch']=5
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9402, 'crossentropy': 0.41803779296875}
store['active_learning_steps'][150]['acquisition']={'indices': [31335, 1010, 22810, 14160, 18790], 'labels': [5, 2, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7215802669525146})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5353315472602844})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5235611200332642})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5314639210700989})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5252335071563721})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5148975849151611})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5529944896697998})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.592099130153656})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5288195610046387})
store['active_learning_steps'][151]['training']['best_epoch']=6
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9406, 'crossentropy': 0.4467115234375}
store['active_learning_steps'][151]['acquisition']={'indices': [6840, 4903, 44378, 34698, 38377], 'labels': [5, -1, 7, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6684635281562805})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.49553364515304565})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.45611870288848877})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5139179229736328})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47212454676628113})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48992788791656494})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.41602431640625}
store['active_learning_steps'][152]['acquisition']={'indices': [50530, 23036, 33633, 9536, 59764], 'labels': [-1, 1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6637033224105835})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4961996078491211})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5095593929290771})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44249427318573})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47493594884872437})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5063627362251282})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47948962450027466})
store['active_learning_steps'][153]['training']['best_epoch']=4
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9399, 'crossentropy': 0.413119091796875}
store['active_learning_steps'][153]['acquisition']={'indices': [20779, 28443, 17293, 9431, 36611], 'labels': [2, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6703227162361145})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5160531997680664})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48778805136680603})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5124461650848389})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46659359335899353})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5297020673751831})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5291216373443604})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5660554766654968})
store['active_learning_steps'][154]['training']['best_epoch']=5
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9401, 'crossentropy': 0.4075749755859375}
store['active_learning_steps'][154]['acquisition']={'indices': [51299, 10268, 5297, 56127, 41532], 'labels': [-1, 1, 2, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6543533205986023})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4643256664276123})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4819113314151764})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46609801054000854})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4723092317581177})
store['active_learning_steps'][155]['training']['best_epoch']=2
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.45145078125}
store['active_learning_steps'][155]['acquisition']={'indices': [43998, 20086, 41530, 34826, 30791], 'labels': [-1, -1, 7, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6432173252105713})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5603387951850891})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5231513977050781})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48831358551979065})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.507426917552948})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5782452821731567})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5235665440559387})
store['active_learning_steps'][156]['training']['best_epoch']=4
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.419459326171875}
store['active_learning_steps'][156]['acquisition']={'indices': [56463, 10182, 11990, 16060, 58004], 'labels': [6, 5, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7010320425033569})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5043335556983948})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5678020715713501})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5021931529045105})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4903196692466736})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5541210174560547})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4835977554321289})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4944732189178467})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.564509928226471})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5490567088127136})
store['active_learning_steps'][157]['training']['best_epoch']=7
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9465, 'crossentropy': 0.4106673828125}
store['active_learning_steps'][157]['acquisition']={'indices': [51016, 4041, 12973, 50499, 56696], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7408274412155151})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5159274339675903})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5180157423019409})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5082907676696777})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46182918548583984})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4940311312675476})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5008761882781982})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5315239429473877})
store['active_learning_steps'][158]['training']['best_epoch']=5
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9455, 'crossentropy': 0.3885177001953125}
store['active_learning_steps'][158]['acquisition']={'indices': [36543, 57153, 6854, 19763, 38443], 'labels': [2, -1, 6, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7092032432556152})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5004782676696777})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.454154908657074})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4717055559158325})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5082430243492126})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47125864028930664})
store['active_learning_steps'][159]['training']['best_epoch']=3
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.40637890625}
store['active_learning_steps'][159]['acquisition']={'indices': [56250, 21455, 32110, 23986, 39912], 'labels': [-1, 5, -1, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6959207057952881})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5012078285217285})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47348475456237793})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47028711438179016})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48445796966552734})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4710402190685272})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48045241832733154})
store['active_learning_steps'][160]['training']['best_epoch']=4
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9382, 'crossentropy': 0.3996276123046875}
store['active_learning_steps'][160]['acquisition']={'indices': [35883, 9044, 9024, 23251, 38425], 'labels': [-1, -1, 6, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6867357492446899})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5190984010696411})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4665570855140686})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44786596298217773})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.491499125957489})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46397632360458374})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48493528366088867})
store['active_learning_steps'][161]['training']['best_epoch']=4
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.406659375}
